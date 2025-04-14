from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import json
import numpy as np
from datetime import datetime

app = Flask(__name__)

# Cấu hình kết nối PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost:5432/recruitment_ahp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Khởi tạo SQLAlchemy
db = SQLAlchemy(app)

# Định nghĩa các model
class RecruitmentRound(db.Model):
    __tablename__ = 'recruitment_rounds'
    round_id = db.Column(db.Integer, primary_key=True)
    round_name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    position = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

class RecruitmentCriteria(db.Model):
    __tablename__ = 'recruitment_criteria'
    criterion_id = db.Column(db.Integer, primary_key=True)
    round_id = db.Column(db.Integer, db.ForeignKey('recruitment_rounds.round_id'), nullable=False)
    criterion_name = db.Column(db.String(100), nullable=False)
    is_custom = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

class CriteriaMatrix(db.Model):
    __tablename__ = 'criteria_matrix'
    matrix_id = db.Column(db.Integer, primary_key=True)
    round_id = db.Column(db.Integer, db.ForeignKey('recruitment_rounds.round_id'), nullable=False)
    matrix_data = db.Column(db.JSON, nullable=False)  # Sử dụng JSON
    consistency_ratio = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

class Candidate(db.Model):
    __tablename__ = 'candidates'
    candidate_id = db.Column(db.Integer, primary_key=True)
    round_id = db.Column(db.Integer, db.ForeignKey('recruitment_rounds.round_id'), nullable=False)
    full_name = db.Column(db.String(255), nullable=False)
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

class CandidateScore(db.Model):
    __tablename__ = 'candidate_scores'
    score_id = db.Column(db.Integer, primary_key=True)
    round_id = db.Column(db.Integer, db.ForeignKey('recruitment_rounds.round_id'), nullable=False)
    candidate_id = db.Column(db.Integer, db.ForeignKey('candidates.candidate_id'), nullable=False)
    total_score = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

# Tiêu chí mặc định
criteria = ["Kiến thức chuyên môn", "Kinh nghiệm", "Kỹ năng mềm", "Tinh thần trách nhiệm", "Mức lương mong muốn", "Phù hợp với văn hóa"]
num_criteria = len(criteria)

# Ma trận so sánh cặp mặc định
default_pairwise = np.array([
    [1, 2, 3, 3, 5, 4],
    [1/2, 1, 2, 2, 4, 3],
    [1/3, 1/2, 1, 2, 3, 2],
    [1/3, 1/2, 1/2, 1, 2, 2],
    [1/5, 1/4, 1/3, 1/2, 1, 1/2],
    [1/4, 1/3, 1/2, 1/2, 2, 1]
])

# Giá trị tối ưu cho từng tiêu chí
optimal_values = np.array([100, 10, 10, 10, 5, 10])

# Kiểm tra kết nối đến database
@app.route('/check_connection')
def check_connection():
    try:
        RecruitmentRound.query.first()
        return "Database connection is successful."
    except Exception as e:
        return f"Database connection failed: {str(e)}"

# Trang chính: Tạo đợt tuyển dụng và nhập thông tin
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Lấy thông tin đợt tuyển dụng
        round_name = request.form['round_name']
        description = request.form['description']
        position = request.form['position']
        num_candidates = int(request.form['num_candidates'])

        # Tạo đợt tuyển dụng mới
        try:
            new_round = RecruitmentRound(
                round_name=round_name,
                description=description,
                position=position
            )
            db.session.add(new_round)
            db.session.commit()

            # Lưu tiêu chí
            for criterion_name in criteria:
                criterion = RecruitmentCriteria(
                    round_id=new_round.round_id,
                    criterion_name=criterion_name
                )
                db.session.add(criterion)
            db.session.commit()

            return render_template('index.html', round_id=new_round.round_id, num_candidates=num_candidates, criteria=criteria, pairwise=default_pairwise, optimal_values=optimal_values)

        except Exception as e:
            db.session.rollback()
            return f"Lỗi khi tạo đợt tuyển dụng: {str(e)}"

    return render_template('index.html', num_candidates=0, criteria=criteria, pairwise=default_pairwise, optimal_values=optimal_values)

# Nhập thông tin ứng viên và so sánh tiêu chí
@app.route('/input/<int:round_id>', methods=['POST'])
def input_candidates(round_id):
    num_candidates = int(request.form['num_candidates'])
    error_message = None

    # Kiểm tra dữ liệu đầu vào
    candidates = []
    try:
        for i in range(num_candidates):
            name = request.form[f'candidate_{i}']
            if not name.strip():  # Kiểm tra tên ứng viên không được để trống
                error_message = f"Tên ứng viên {i + 1} không được để trống."
                raise ValueError(error_message)

            values = []
            for j in range(num_criteria):
                value_str = request.form.get(f'candidate_{i}_criterion_{j}', '')
                if not value_str.strip():  # Kiểm tra trường điểm không được để trống
                    error_message = f"Điểm '{criteria[j]}' của ứng viên {i + 1} không được để trống."
                    raise ValueError(error_message)

                value = float(value_str)
                if value < 0:  # Điểm không được âm
                    error_message = f"Điểm '{criteria[j]}' của ứng viên {i + 1} không được nhỏ hơn 0."
                    raise ValueError(error_message)

                if value > optimal_values[j]:  # Kiểm tra điểm không vượt quá giá trị tối đa
                    error_message = f"Điểm '{criteria[j]}' của ứng viên {i + 1} vượt quá giá trị tối đa ({optimal_values[j]})."
                    raise ValueError(error_message)

                values.append(value)

            candidates.append({'name': name, 'values': values})

    except ValueError as e:
        # Nếu có lỗi, trả về trang index.html với thông báo lỗi
        return render_template('index.html', round_id=round_id, num_candidates=num_candidates, criteria=criteria, pairwise=default_pairwise, optimal_values=optimal_values, error_message=str(e))

    # Nếu không có lỗi, tiến hành lưu dữ liệu
    try:
        for candidate_data in candidates:
            name = candidate_data['name']
            values = candidate_data['values']
            candidate = Candidate(
                round_id=round_id,
                full_name=name,
                notes="N/A"
            )
            db.session.add(candidate)
            db.session.commit()
            candidate_data['id'] = candidate.candidate_id

    except Exception as e:
        db.session.rollback()
        return f"Lỗi khi lưu ứng viên: {str(e)}"

    # Lấy ma trận so sánh cặp từ form
    pairwise = np.zeros((num_criteria, num_criteria))
    for i in range(num_criteria):
        for j in range(num_criteria):
            pairwise[i][j] = float(request.form[f'pairwise_{i}_{j}'])

    # Tính toán AHP
    try:
        # 1. Tính trọng số tiêu chí
        col_sums = np.sum(pairwise, axis=0)
        normalized_matrix = pairwise / col_sums
        weights = np.mean(normalized_matrix, axis=1)

        # 2. Kiểm tra tính nhất quán
        lambda_max = np.sum(col_sums * weights)
        ci = (lambda_max - num_criteria) / (num_criteria - 1)
        cr = ci / 1.24  # RI = 1.24 cho 6 tiêu chí

        # Lưu ma trận so sánh tiêu chí
        matrix_data = json.dumps({"matrix": pairwise.tolist()})
        criteria_matrix = CriteriaMatrix(
            round_id=round_id,
            matrix_data=matrix_data,
            consistency_ratio=cr
        )
        db.session.add(criteria_matrix)
        db.session.commit()

        # 3. Tính giá trị chuẩn hóa và xếp hạng
        banding = np.array([c['values'] for c in candidates]) / optimal_values
        banding_sums = np.sum(banding, axis=0)
        candidate_weights = banding / banding_sums
        scores = np.sum(candidate_weights * weights, axis=1)

        # 4. Xếp hạng và lưu vào bảng candidate_scores
        ranked = sorted(zip([c['id'] for c in candidates], [c['name'] for c in candidates], scores), key=lambda x: x[2], reverse=True)
        for rank, (candidate_id, name, score) in enumerate(ranked, 1):
            candidate_score = CandidateScore(
                round_id=round_id,
                candidate_id=candidate_id,
                total_score=score,
                ranking=rank
            )
            db.session.add(candidate_score)
        db.session.commit()

    except Exception as e:
        db.session.rollback()
        return f"Lỗi khi tính toán AHP: {str(e)}"

    # Trả kết quả
    ranked_display = [(name, score) for _, name, score in ranked]
    return render_template('results.html', round_id=round_id, weights=weights, criteria=criteria, cr=cr, ranked=ranked_display)

# Xem lịch sử đợt tuyển dụng
@app.route('/history')
def history():
    rounds = RecruitmentRound.query.all()
    return render_template('history.html', rounds=rounds)

# Xem chi tiết đợt tuyển dụng
@app.route('/round/<int:round_id>')
def round_detail(round_id):
    round = RecruitmentRound.query.get_or_404(round_id)
    criteria_list = RecruitmentCriteria.query.filter_by(round_id=round_id).all()
    matrix = CriteriaMatrix.query.filter_by(round_id=round_id).first()
    candidates = Candidate.query.filter_by(round_id=round_id).all()
    scores = CandidateScore.query.filter_by(round_id=round_id).order_by(CandidateScore.ranking).all()

    # Xử lý matrix_data (vì cột là db.JSON, dữ liệu trả về là chuỗi)
    if matrix and isinstance(matrix.matrix_data, str):
        try:
            matrix.matrix_data = json.loads(matrix.matrix_data)
        except json.JSONDecodeError:
            matrix.matrix_data = {"matrix": []}  # Giá trị mặc định nếu không phân tích được
    elif not matrix:
        matrix = CriteriaMatrix(matrix_data={"matrix": []}, consistency_ratio=0.0)  # Giá trị mặc định nếu matrix không tồn tại

    # Lấy tên ứng viên từ candidate_id trong scores
    ranked = []
    for score in scores:
        candidate = Candidate.query.get(score.candidate_id)
        ranked.append((candidate.full_name, score.total_score))

    return render_template('round_detail.html', round=round, criteria=criteria_list, matrix=matrix, candidates=candidates, ranked=ranked)

# Xóa đợt tuyển dụng
@app.route('/delete_round/<int:round_id>')
def delete_round(round_id):
    try:
        # Xóa dữ liệu liên quan trước
        CandidateScore.query.filter_by(round_id=round_id).delete()
        Candidate.query.filter_by(round_id=round_id).delete()
        CriteriaMatrix.query.filter_by(round_id=round_id).delete()
        RecruitmentCriteria.query.filter_by(round_id=round_id).delete()
        RecruitmentRound.query.filter_by(round_id=round_id).delete()
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return f"Lỗi khi xóa đợt tuyển dụng: {str(e)}"

    return redirect(url_for('history'))

if __name__ == '__main__':
    app.run(debug=True)