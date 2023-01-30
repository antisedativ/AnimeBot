CREATE TABLE users (
    id INT PRIMARY KEY,
    username VARCHAR(255),
    firstname VARCHAR(255),
    lastname VARCHAR(255),
    chat_id INT,
    last_message_date TIMESTAMP
);