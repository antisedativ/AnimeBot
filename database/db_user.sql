CREATE TABLE users (
    chat_id BIGINT PRIMARY KEY,
    username VARCHAR(255),
    firstname VARCHAR(255),
    lastname VARCHAR(255),
    last_message_date TIMESTAMP
);