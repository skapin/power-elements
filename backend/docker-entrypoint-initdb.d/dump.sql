--
-- PostgreSQL database dump
--

-- Dumped from database version 12.2 (Debian 12.2-1.pgdg100+1)
-- Dumped by pg_dump version 12.2 (Debian 12.2-1.pgdg100+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
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
-- Name: account; Type: TABLE; Schema: public; Owner: aiosuperusercovid
--

CREATE TABLE public.account (
    uniqid character varying(36) NOT NULL,
    password character varying(89),
    name character varying(50),
    created_at timestamp without time zone
);


ALTER TABLE public.account OWNER TO aiosuperusercovid;

--
-- Name: question; Type: TABLE; Schema: public; Owner: aiosuperusercovid
--

CREATE TABLE public.question (
    uniqid character varying(36) NOT NULL,
    name character varying(255) NOT NULL,
    created_at timestamp without time zone
);


ALTER TABLE public.question OWNER TO aiosuperusercovid;

--
-- Name: response; Type: TABLE; Schema: public; Owner: aiosuperusercovid
--

CREATE TABLE public.response (
    uniqid character varying(36) NOT NULL,
    value integer,
    created_at timestamp without time zone,
    question_id character varying(36),
    account_id character varying(36)
);


ALTER TABLE public.response OWNER TO aiosuperusercovid;

--
-- Data for Name: account; Type: TABLE DATA; Schema: public; Owner: aiosuperusercovid
--

COPY public.account (uniqid, password, name, created_at) FROM stdin;
\.


--
-- Data for Name: question; Type: TABLE DATA; Schema: public; Owner: aiosuperusercovid
--

COPY public.question (uniqid, name, created_at) FROM stdin;
3783f190-db0f-4a28-9b50-fcecbd17e69f	Te sens tu malade ce matin ?	2020-04-30 07:16:55.016391
89ea569a-f678-4618-82d6-d0a4fdc8b05f	Penses-tu avoir de la fièvre ?	2020-04-30 07:16:55.034856
2ba62fc8-cf9e-458b-94c9-5e189310a984	As-tu une sensation de fatigue ?	2020-04-30 07:16:55.039714
a719ad25-487c-4f59-b303-6d20868b918d	As-tu de la toux sèche ?	2020-04-30 07:16:55.042668
7c12b862-5522-40b8-a29d-5152555cb2bf	As-tu des courbatures et des douleurs ?	2020-04-30 07:16:55.044663
1b7066d0-72b5-4a6d-9003-54a9e05e13a4	As-tu le nez bouché ou as-tu le nez qui coule ?	2020-04-30 07:16:55.0485
3746c93e-a501-4901-b9af-8659e7ae73df	As-tu des maux de gorge ?	2020-04-30 07:16:55.05309
\.


--
-- Data for Name: response; Type: TABLE DATA; Schema: public; Owner: aiosuperusercovid
--

COPY public.response (uniqid, value, created_at, question_id, account_id) FROM stdin;
\.


--
-- Name: account account_name_key; Type: CONSTRAINT; Schema: public; Owner: aiosuperusercovid
--

ALTER TABLE ONLY public.account
    ADD CONSTRAINT account_name_key UNIQUE (name);


--
-- Name: account account_pkey; Type: CONSTRAINT; Schema: public; Owner: aiosuperusercovid
--

ALTER TABLE ONLY public.account
    ADD CONSTRAINT account_pkey PRIMARY KEY (uniqid);


--
-- Name: question question_pkey; Type: CONSTRAINT; Schema: public; Owner: aiosuperusercovid
--

ALTER TABLE ONLY public.question
    ADD CONSTRAINT question_pkey PRIMARY KEY (uniqid);


--
-- Name: response response_pkey; Type: CONSTRAINT; Schema: public; Owner: aiosuperusercovid
--

ALTER TABLE ONLY public.response
    ADD CONSTRAINT response_pkey PRIMARY KEY (uniqid);


--
-- Name: response response_account_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: aiosuperusercovid
--

ALTER TABLE ONLY public.response
    ADD CONSTRAINT response_account_id_fkey FOREIGN KEY (account_id) REFERENCES public.account(uniqid) ON UPDATE CASCADE;


--
-- Name: response response_question_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: aiosuperusercovid
--

ALTER TABLE ONLY public.response
    ADD CONSTRAINT response_question_id_fkey FOREIGN KEY (question_id) REFERENCES public.question(uniqid) ON UPDATE CASCADE;


--
-- PostgreSQL database dump complete
--

