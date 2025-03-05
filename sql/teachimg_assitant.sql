CREATE DATABASE teaching_assistant;
SHOW DATABASES;
USE teaching_assistant;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,        -- 唯一主鍵
    line_user_id VARCHAR(255) NOT NULL UNIQUE, -- LINE 的用戶唯一 ID
    name VARCHAR(255),                        -- 用戶名稱
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- 註冊時間
);

CREATE TABLE sessions (
    id INT AUTO_INCREMENT PRIMARY KEY,        -- 唯一主鍵
    user_id INT NOT NULL,                     -- 關聯到 users 表
    session_data JSON,                        -- 儲存對話上下文的 JSON 數據
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- 會話開始時間
    FOREIGN KEY (user_id) REFERENCES users(id) -- 外鍵約束
);

CREATE TABLE teaching_content (
    id INT AUTO_INCREMENT PRIMARY KEY,        -- 唯一主鍵
    user_id INT NOT NULL,                     -- 關聯到 users 表
    topic VARCHAR(255) NOT NULL,              -- 教學主題
    content TEXT NOT NULL,                    -- 教學內容
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- 生成時間
    FOREIGN KEY (user_id) REFERENCES users(id) -- 外鍵約束
);

CREATE TABLE quiz_results (
    id INT AUTO_INCREMENT PRIMARY KEY,        -- 唯一主鍵
    user_id INT NOT NULL,                     -- 關聯到 users 表
    quiz_data JSON NOT NULL,                  -- 測驗內容和答案
    score INT,                                -- 得分
    completed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- 完成時間
    FOREIGN KEY (user_id) REFERENCES users(id) -- 外鍵約束
);

CREATE TABLE error_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,        -- 唯一主鍵
    user_id INT,                              -- 可選，關聯到 users 表
    error_message TEXT NOT NULL,              -- 錯誤信息
    occurred_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- 發生時間
);

mysqldump -u root -p --no-data teaching_assistant > 001_create_tables.sql
