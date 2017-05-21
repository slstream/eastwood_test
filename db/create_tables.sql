\c eastwood

-- Таблица Должность
CREATE TABLE IF NOT EXISTS "public"."position" (
  id SERIAL NOT NULL PRIMARY KEY,
  name VARCHAR(40) NOT NULL UNIQUE
);

-- Таблица Отдел
CREATE TABLE IF NOT EXISTS "public"."department" (
  id SERIAL NOT NULL PRIMARY KEY,
  name VARCHAR(40) NOT NULL UNIQUE
);

-- Таблица Сотрудник
CREATE TABLE IF NOT EXISTS "public"."employee" (
  id SERIAL NOT NULL PRIMARY KEY,
  first_name VARCHAR(40) NOT NULL,
  second_name VARCHAR(40) NOT NULL,
  birthday DATE NOT NULL,
  email VARCHAR(40) NOT NULL,
  start_date DATE NOT NULL DEFAULT timezone('utc'::text, now()),
  finish_date DATE,
  position_id INTEGER NOT NULL,
  department_id INTEGER NOT NULL
);

ALTER TABLE IF EXISTS "public"."employee" ADD CONSTRAINT fk_employee_position
  FOREIGN KEY (position_id) REFERENCES "public"."position"(id);

ALTER TABLE IF EXISTS "public"."employee" ADD CONSTRAINT fk_employee_department
  FOREIGN KEY (department_id) REFERENCES "public"."department"(id);