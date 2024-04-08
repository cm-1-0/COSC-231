CREATE DATABASE IF NOT EXISTS MoneyMinder;
USE MoneyMinder;

CREATE TABLE User (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE FinancialAccount (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    balance DECIMAL(10, 2),
    FOREIGN KEY (user_id) REFERENCES User(id)
);

CREATE TABLE BudgetCategory (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    name VARCHAR(255),
    FOREIGN KEY (user_id) REFERENCES User(id)
);

CREATE TABLE SavingsGoal (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    target_amount DECIMAL(10, 2),
    FOREIGN KEY (user_id) REFERENCES User(id)
);

CREATE TABLE Transaction (
    id INT AUTO_INCREMENT PRIMARY KEY,
    account_id INT,
    amount DECIMAL(10, 2),
    FOREIGN KEY (account_id) REFERENCES FinancialAccount(id)
);