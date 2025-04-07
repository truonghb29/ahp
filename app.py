from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

# Tiêu chí
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

# Giá trị tối ưu cho từng tiêu chí (giả định)
optimal_values = np.array([100, 10, 10, 10, 5, 10])

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        num_candidates = int(request.form['num_candidates'])
        return render_template('index.html', num_candidates=num_candidates, criteria=criteria, pairwise=default_pairwise)
    return render_template('index.html', num_candidates=0, criteria=criteria, pairwise=default_pairwise)

@app.route('/calculate', methods=['POST'])
def calculate():
    num_candidates = int(request.form['num_candidates'])
    
    # Lấy dữ liệu ứng viên
    candidates = []
    for i in range(num_candidates):
        name = request.form[f'candidate_{i}']
        values = [float(request.form[f'candidate_{i}_criterion_{j}']) for j in range(num_criteria)]
        candidates.append({'name': name, 'values': values})
    
    # Lấy ma trận so sánh cặp từ form
    pairwise = np.zeros((num_criteria, num_criteria))
    for i in range(num_criteria):
        for j in range(num_criteria):
            pairwise[i][j] = float(request.form[f'pairwise_{i}_{j}'])

    # 1. Tính trọng số tiêu chí
    col_sums = np.sum(pairwise, axis=0)
    normalized_matrix = pairwise / col_sums
    weights = np.mean(normalized_matrix, axis=1)

    # 2. Kiểm tra tính nhất quán
    lambda_max = np.sum(col_sums * weights)
    ci = (lambda_max - num_criteria) / (num_criteria - 1)
    cr = ci / 1.24  # RI = 1.24 cho 6 tiêu chí

    # 3. Tính giá trị chuẩn hóa và xếp hạng
    banding = np.array([c['values'] for c in candidates]) / optimal_values
    banding_sums = np.sum(banding, axis=0)
    candidate_weights = banding / banding_sums
    scores = np.sum(candidate_weights * weights, axis=1)

    # 4. Xếp hạng
    ranked = sorted(zip([c['name'] for c in candidates], scores), key=lambda x: x[1], reverse=True)

    # 5. Trả kết quả
    return render_template('results.html', weights=weights, criteria=criteria, cr=cr, ranked=ranked)

if __name__ == '__main__':
    app.run(debug=True)