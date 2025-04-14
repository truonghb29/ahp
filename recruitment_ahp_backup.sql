--
-- PostgreSQL database dump
--

-- Dumped from database version 17.4
-- Dumped by pg_dump version 17.4

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: candidate_comparisons; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.candidate_comparisons (
    comparison_id integer NOT NULL,
    round_id integer,
    criterion_id integer,
    comparison_data jsonb NOT NULL,
    consistency_ratio double precision NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT candidate_comparisons_consistency_ratio_check CHECK ((consistency_ratio >= (0)::double precision))
);


ALTER TABLE public.candidate_comparisons OWNER TO postgres;

--
-- Name: candidate_comparisons_comparison_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.candidate_comparisons_comparison_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.candidate_comparisons_comparison_id_seq OWNER TO postgres;

--
-- Name: candidate_comparisons_comparison_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.candidate_comparisons_comparison_id_seq OWNED BY public.candidate_comparisons.comparison_id;


--
-- Name: candidate_scores; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.candidate_scores (
    score_id integer NOT NULL,
    round_id integer,
    candidate_id integer,
    total_score double precision NOT NULL,
    ranking integer NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT candidate_scores_ranking_check CHECK ((ranking > 0)),
    CONSTRAINT candidate_scores_total_score_check CHECK ((total_score >= (0)::double precision))
);


ALTER TABLE public.candidate_scores OWNER TO postgres;

--
-- Name: candidate_scores_score_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.candidate_scores_score_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.candidate_scores_score_id_seq OWNER TO postgres;

--
-- Name: candidate_scores_score_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.candidate_scores_score_id_seq OWNED BY public.candidate_scores.score_id;


--
-- Name: candidates; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.candidates (
    candidate_id integer NOT NULL,
    round_id integer,
    full_name character varying(255) NOT NULL,
    notes text,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.candidates OWNER TO postgres;

--
-- Name: candidates_candidate_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.candidates_candidate_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.candidates_candidate_id_seq OWNER TO postgres;

--
-- Name: candidates_candidate_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.candidates_candidate_id_seq OWNED BY public.candidates.candidate_id;


--
-- Name: criteria_matrix; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.criteria_matrix (
    matrix_id integer NOT NULL,
    round_id integer,
    matrix_data jsonb NOT NULL,
    consistency_ratio double precision NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT criteria_matrix_consistency_ratio_check CHECK ((consistency_ratio >= (0)::double precision))
);


ALTER TABLE public.criteria_matrix OWNER TO postgres;

--
-- Name: criteria_matrix_matrix_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.criteria_matrix_matrix_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.criteria_matrix_matrix_id_seq OWNER TO postgres;

--
-- Name: criteria_matrix_matrix_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.criteria_matrix_matrix_id_seq OWNED BY public.criteria_matrix.matrix_id;


--
-- Name: recruitment_criteria; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.recruitment_criteria (
    criterion_id integer NOT NULL,
    round_id integer,
    criterion_name character varying(100) NOT NULL,
    is_custom boolean DEFAULT false,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.recruitment_criteria OWNER TO postgres;

--
-- Name: recruitment_criteria_criterion_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.recruitment_criteria_criterion_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.recruitment_criteria_criterion_id_seq OWNER TO postgres;

--
-- Name: recruitment_criteria_criterion_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.recruitment_criteria_criterion_id_seq OWNED BY public.recruitment_criteria.criterion_id;


--
-- Name: recruitment_rounds; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.recruitment_rounds (
    round_id integer NOT NULL,
    round_name character varying(255) NOT NULL,
    description text,
    "position" character varying(100) NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.recruitment_rounds OWNER TO postgres;

--
-- Name: recruitment_rounds_round_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.recruitment_rounds_round_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.recruitment_rounds_round_id_seq OWNER TO postgres;

--
-- Name: recruitment_rounds_round_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.recruitment_rounds_round_id_seq OWNED BY public.recruitment_rounds.round_id;


--
-- Name: candidate_comparisons comparison_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.candidate_comparisons ALTER COLUMN comparison_id SET DEFAULT nextval('public.candidate_comparisons_comparison_id_seq'::regclass);


--
-- Name: candidate_scores score_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.candidate_scores ALTER COLUMN score_id SET DEFAULT nextval('public.candidate_scores_score_id_seq'::regclass);


--
-- Name: candidates candidate_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.candidates ALTER COLUMN candidate_id SET DEFAULT nextval('public.candidates_candidate_id_seq'::regclass);


--
-- Name: criteria_matrix matrix_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.criteria_matrix ALTER COLUMN matrix_id SET DEFAULT nextval('public.criteria_matrix_matrix_id_seq'::regclass);


--
-- Name: recruitment_criteria criterion_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.recruitment_criteria ALTER COLUMN criterion_id SET DEFAULT nextval('public.recruitment_criteria_criterion_id_seq'::regclass);


--
-- Name: recruitment_rounds round_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.recruitment_rounds ALTER COLUMN round_id SET DEFAULT nextval('public.recruitment_rounds_round_id_seq'::regclass);


--
-- Data for Name: candidate_comparisons; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.candidate_comparisons (comparison_id, round_id, criterion_id, comparison_data, consistency_ratio, created_at) FROM stdin;
1	1	1	{"matrix": [[1, 2, 4], [0.5, 1, 2], [0.25, 0.5, 1]]}	0.07	2025-04-15 01:18:40.318789
\.


--
-- Data for Name: candidate_scores; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.candidate_scores (score_id, round_id, candidate_id, total_score, ranking, created_at) FROM stdin;
1	1	1	0.45	1	2025-04-15 01:18:40.318789
2	1	2	0.35	2	2025-04-15 01:18:40.318789
3	1	3	0.2	3	2025-04-15 01:18:40.318789
4	2	4	0.5673349066466837	1	2025-04-15 02:24:11.662479
5	2	5	0.4326650933533161	2	2025-04-15 02:24:11.662479
6	2	6	0.5673349066466837	1	2025-04-15 02:27:29.059144
7	2	7	0.4326650933533161	2	2025-04-15 02:27:29.059144
\.


--
-- Data for Name: candidates; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.candidates (candidate_id, round_id, full_name, notes, created_at) FROM stdin;
1	1	Nguyễn Văn A	Có kinh nghiệm 2 năm	2025-04-15 01:18:40.318789
2	1	Trần Thị B	Tốt nghiệp loại giỏi	2025-04-15 01:18:40.318789
3	1	Lê Văn C	Có chứng chỉ quốc tế	2025-04-15 01:18:40.318789
4	2	Nguyễn Thanh Trường	N/A	2025-04-15 02:24:11.651694
5	2	Phạm Thế Anh	N/A	2025-04-15 02:24:11.655084
6	2	Nguyễn Thanh Trường	N/A	2025-04-15 02:27:29.053648
7	2	Phạm Thế Anh	N/A	2025-04-15 02:27:29.055509
\.


--
-- Data for Name: criteria_matrix; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.criteria_matrix (matrix_id, round_id, matrix_data, consistency_ratio, created_at) FROM stdin;
1	1	{"matrix": [[1, 3, 5], [0.33, 1, 2], [0.2, 0.5, 1]]}	0.08	2025-04-15 01:18:40.318789
2	2	"{\\"matrix\\": [[1.0, 2.0, 3.0, 3.0, 5.0, 4.0], [0.5, 1.0, 2.0, 2.0, 4.0, 3.0], [0.33, 0.5, 1.0, 2.0, 3.0, 2.0], [0.33, 0.5, 0.5, 1.0, 2.0, 2.0], [0.2, 0.25, 0.33, 0.5, 1.0, 0.5], [0.25, 0.33, 0.5, 0.5, 2.0, 1.0]]}"	0.02134368800944681	2025-04-15 02:24:11.65771
3	2	"{\\"matrix\\": [[1.0, 2.0, 3.0, 3.0, 5.0, 4.0], [0.5, 1.0, 2.0, 2.0, 4.0, 3.0], [0.33, 0.5, 1.0, 2.0, 3.0, 2.0], [0.33, 0.5, 0.5, 1.0, 2.0, 2.0], [0.2, 0.25, 0.33, 0.5, 1.0, 0.5], [0.25, 0.33, 0.5, 0.5, 2.0, 1.0]]}"	0.02134368800944681	2025-04-15 02:27:29.057078
\.


--
-- Data for Name: recruitment_criteria; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.recruitment_criteria (criterion_id, round_id, criterion_name, is_custom, created_at) FROM stdin;
1	1	Kỹ năng lập trình	f	2025-04-15 01:18:40.318789
2	1	Kinh nghiệm làm việc	f	2025-04-15 01:18:40.318789
3	1	Kỹ năng giao tiếp	t	2025-04-15 01:18:40.318789
4	2	Kiến thức chuyên môn	f	2025-04-15 02:23:19.011842
5	2	Kinh nghiệm	f	2025-04-15 02:23:19.011842
6	2	Kỹ năng mềm	f	2025-04-15 02:23:19.011842
7	2	Tinh thần trách nhiệm	f	2025-04-15 02:23:19.011842
8	2	Mức lương mong muốn	f	2025-04-15 02:23:19.011842
9	2	Phù hợp với văn hóa	f	2025-04-15 02:23:19.011842
\.


--
-- Data for Name: recruitment_rounds; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.recruitment_rounds (round_id, round_name, description, "position", created_at) FROM stdin;
1	Tuyển dụng kỹ sư phần mềm 2025	Đợt tuyển dụng tháng 4	Kỹ sư phần mềm	2025-04-15 01:18:40.318789
2	Tuyển Dụng Những Thằng Lười	Tìm người lười 	Leader	2025-04-15 02:23:19.007083
\.


--
-- Name: candidate_comparisons_comparison_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.candidate_comparisons_comparison_id_seq', 1, true);


--
-- Name: candidate_scores_score_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.candidate_scores_score_id_seq', 7, true);


--
-- Name: candidates_candidate_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.candidates_candidate_id_seq', 7, true);


--
-- Name: criteria_matrix_matrix_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.criteria_matrix_matrix_id_seq', 3, true);


--
-- Name: recruitment_criteria_criterion_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.recruitment_criteria_criterion_id_seq', 33, true);


--
-- Name: recruitment_rounds_round_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.recruitment_rounds_round_id_seq', 6, true);


--
-- Name: candidate_comparisons candidate_comparisons_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.candidate_comparisons
    ADD CONSTRAINT candidate_comparisons_pkey PRIMARY KEY (comparison_id);


--
-- Name: candidate_scores candidate_scores_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.candidate_scores
    ADD CONSTRAINT candidate_scores_pkey PRIMARY KEY (score_id);


--
-- Name: candidates candidates_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.candidates
    ADD CONSTRAINT candidates_pkey PRIMARY KEY (candidate_id);


--
-- Name: criteria_matrix criteria_matrix_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.criteria_matrix
    ADD CONSTRAINT criteria_matrix_pkey PRIMARY KEY (matrix_id);


--
-- Name: recruitment_criteria recruitment_criteria_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.recruitment_criteria
    ADD CONSTRAINT recruitment_criteria_pkey PRIMARY KEY (criterion_id);


--
-- Name: recruitment_rounds recruitment_rounds_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.recruitment_rounds
    ADD CONSTRAINT recruitment_rounds_pkey PRIMARY KEY (round_id);


--
-- Name: candidate_comparisons candidate_comparisons_criterion_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.candidate_comparisons
    ADD CONSTRAINT candidate_comparisons_criterion_id_fkey FOREIGN KEY (criterion_id) REFERENCES public.recruitment_criteria(criterion_id) ON DELETE CASCADE;


--
-- Name: candidate_comparisons candidate_comparisons_round_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.candidate_comparisons
    ADD CONSTRAINT candidate_comparisons_round_id_fkey FOREIGN KEY (round_id) REFERENCES public.recruitment_rounds(round_id) ON DELETE CASCADE;


--
-- Name: candidate_scores candidate_scores_candidate_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.candidate_scores
    ADD CONSTRAINT candidate_scores_candidate_id_fkey FOREIGN KEY (candidate_id) REFERENCES public.candidates(candidate_id) ON DELETE CASCADE;


--
-- Name: candidate_scores candidate_scores_round_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.candidate_scores
    ADD CONSTRAINT candidate_scores_round_id_fkey FOREIGN KEY (round_id) REFERENCES public.recruitment_rounds(round_id) ON DELETE CASCADE;


--
-- Name: candidates candidates_round_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.candidates
    ADD CONSTRAINT candidates_round_id_fkey FOREIGN KEY (round_id) REFERENCES public.recruitment_rounds(round_id) ON DELETE CASCADE;


--
-- Name: criteria_matrix criteria_matrix_round_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.criteria_matrix
    ADD CONSTRAINT criteria_matrix_round_id_fkey FOREIGN KEY (round_id) REFERENCES public.recruitment_rounds(round_id) ON DELETE CASCADE;


--
-- Name: recruitment_criteria recruitment_criteria_round_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.recruitment_criteria
    ADD CONSTRAINT recruitment_criteria_round_id_fkey FOREIGN KEY (round_id) REFERENCES public.recruitment_rounds(round_id) ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

