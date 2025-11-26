-- Step 1: Drop old table if exists
DROP TABLE IF EXISTS Employee;

-- Step 2: Create new table with correct column types
CREATE TABLE Employee (
    EmpID VARCHAR(10) PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Designation VARCHAR(100),
    City VARCHAR(100),
    Blood_Group VARCHAR(10),
    Gender VARCHAR(10),
    Salary INT
);

-- Step 3: Insert all 30 records
INSERT INTO Employee VALUES
('EMP001', 'Sara', 'Software Engineer', 'Noida', 'AB+', 'Male', 37714),
('EMP002', 'Vivek', 'System Administrator', 'Surat', 'A+', 'Male', 83183),
('EMP003', 'Aanya', 'Software Engineer', 'Noida', 'AB+', 'Male', 87490),
('EMP004', 'Shreya', 'Data Analyst', 'Noida', 'A+', 'Female', 66337),
('EMP005', 'Vikram', 'System Administrator', 'Bangalore', 'O+', 'Female', 36152),
('EMP006', 'Sahil', 'Software Engineer', 'Indore', 'AB+', 'Female', 99067),
('EMP007', 'Kabir', 'Project Manager', 'Hyderabad', 'O+', 'Male', 67972),
('EMP008', 'Tara', 'UI/UX Designer', 'Trivandrum', 'O+', 'Male', 81761),
('EMP009', 'Simran', 'UI/UX Designer', 'Hyderabad', 'O+', 'Male', 118704),
('EMP010', 'Kabir', 'Software Engineer', 'Surat', 'B+', 'Male', 149439),
('EMP011', 'Nidhi', 'Software Engineer', 'Delhi', 'B+', 'Female', 67500),
('EMP012', 'Pranav', 'DevOps Engineer', 'Mumbai', 'A+', 'Male', 85200),
('EMP013', 'Riya', 'Data Scientist', 'Pune', 'O+', 'Female', 98000),
('EMP014', 'Arjun', 'Database Administrator', 'Kolkata', 'AB+', 'Male', 72000),
('EMP015', 'Neha', 'Software Engineer', 'Jaipur', 'B+', 'Female', 64000),
('EMP016', 'Rakesh', 'System Engineer', 'Lucknow', 'O-', 'Male', 59000),
('EMP017', 'Ananya', 'Frontend Developer', 'Chennai', 'A-', 'Female', 71000),
('EMP018', 'Manoj', 'Backend Developer', 'Coimbatore', 'O+', 'Male', 78000),
('EMP019', 'Rohit', 'Software Engineer', 'Pune', 'B+', 'Male', 83500),
('EMP020', 'Sneha', 'Software Tester', 'Delhi', 'A+', 'Female', 56000),
('EMP021', 'Amit', 'Project Manager', 'Bangalore', 'O+', 'Male', 98000),
('EMP022', 'Divya', 'Business Analyst', 'Hyderabad', 'B-', 'Female', 75500),
('EMP023', 'Naveen', 'Network Engineer', 'Chennai', 'O+', 'Male', 69000),
('EMP024', 'Pooja', 'HR Manager', 'Delhi', 'A+', 'Female', 62000),
('EMP025', 'Raman', 'Software Engineer', 'Noida', 'AB+', 'Male', 72000),
('EMP026', 'Kiran', 'UI Designer', 'Pune', 'O-', 'Female', 68000),
('EMP027', 'Varun', 'Data Engineer', 'Chennai', 'B+', 'Male', 94000),
('EMP028', 'Isha', 'Software Developer', 'Hyderabad', 'A+', 'Female', 81000),
('EMP029', 'Aditya', 'System Administrator', 'Mumbai', 'O+', 'Male', 87500),
('EMP030', 'Priya', 'Data Analyst', 'Kolkata', 'B+', 'Female', 70000);

-- Step 4: Display data
SELECT * FROM Employee;
select EmpID,Name employee,
case
When Salary>20000 then "A"
When Salary>30000 then "B"
When Salary>40000 then "C"
when Salary>50000 then "D"
When Salary>60000 then "O"
else "E"
end as Grade from employee;
select * from Employee where employee = (min(salary) from Employee);