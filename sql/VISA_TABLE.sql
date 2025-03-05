SHOW DATABASES;
CREATE DATABASE study_abroad_assitant;
SHOW DATABASES;
USE study_abroad_assitant;

SHOW Tables;

CREATE TABLE Visa_Requirements (
    Visa_ID INT AUTO_INCREMENT PRIMARY KEY,
    Country VARCHAR(50) NOT NULL,
    Country_Code VARCHAR(10) NOT NULL,
    Visa_Type VARCHAR(100) NOT NULL,
    Required_Documents TEXT,
    Fees_USD DECIMAL(10, 2),
    Processing_Time VARCHAR(50),
    Validity VARCHAR(50),
    Application_Process TEXT,
    Official_Link TEXT,
    Last_Updated DATETIME DEFAULT CURRENT_TIMESTAMP
);


INSERT INTO Visa_Requirements (
    Country, Country_Code, Visa_Type, Required_Documents, Fees_USD, 
    Processing_Time, Validity, Application_Process, Official_Link
)
VALUES 
    -- United States
    ('United States', 'USA', 'F-1 Student Visa', 
     'Passport, DS-160 Form, I-20 Form, SEVIS Fee Receipt, Proof of Funds, Photo', 
     185.00, 
     'Approximately 23 days', 
     'Course duration + 60 days', 
     '1. Obtain admission to a SEVP-approved U.S. institution and receive the I-20 form. 2. Pay the SEVIS I-901 fee. 3. Complete the DS-160 online visa application. 4. Pay the visa application fee. 5. Schedule and attend a visa interview at the American Institute in Taiwan (AIT).', 
     'https://www.ait.org.tw/visas/nonimmigrant-visas/'),

    -- United Kingdom
    ('United Kingdom', 'UK', 'Student Visa', 
     'Passport, Confirmation of Acceptance for Studies (CAS), Financial Proof, Tuberculosis Test Results', 
     450.00, 
     '3-4 weeks', 
     'Course duration + 4 months', 
     '1. Obtain a CAS from a UK institution. 2. Complete the online visa application. 3. Pay the visa fee and healthcare surcharge. 4. Schedule and attend a biometric appointment.', 
     'https://www.gov.uk/student-visa'),

    -- Australia
    ('Australia', 'AUS', 'Student Visa (Subclass 500)', 
     'Passport, Confirmation of Enrolment (CoE), Financial Proof, Health Insurance', 
     1068.00, 
     '4-6 weeks', 
     'Course duration + 2 months', 
     '1. Obtain a CoE from an Australian institution. 2. Complete the online visa application. 3. Pay the visa application fee. 4. Undergo a health examination if required.', 
     'https://immi.homeaffairs.gov.au/visas/getting-a-visa/visa-listing/student-500'),

    -- Japan
    ('Japan', 'JP', 'Student Visa', 
     'Passport, Certificate of Eligibility, Proof of Funds', 
     30.00, 
     '2-3 weeks', 
     'Course duration', 
     '1. Obtain a Certificate of Eligibility from the Japanese institution. 2. Submit the visa application at the Japanese embassy or consulate in Taiwan.', 
     'https://www.mofa.go.jp/j_info/visit/visa/'),

    -- South Korea
    ('South Korea', 'KR', 'D-2 Student Visa', 
     'Passport, Certificate of Admission, Proof of Financial Capability', 
     50.00, 
     '1-2 weeks', 
     'Course duration', 
     '1. Obtain a Certificate of Admission from a Korean institution. 2. Submit the visa application at the Korean embassy or consulate in Taiwan.', 
     'https://www.studyinkorea.go.kr/en/sub/overseas_info/visa.do'),

    -- Singapore
    ('Singapore', 'SG', 'Student Pass', 
     'Passport, Admission Letter, Financial Proof', 
     30.00, 
     '1-2 weeks', 
     'Course duration', 
     '1. Obtain an admission letter from a Singaporean institution. 2. Apply for a Student Pass through the Immigration & Checkpoints Authority (ICA).', 
     'https://www.ica.gov.sg/pass/studentpass/apply'),

    -- Thailand
    ('Thailand', 'TH', 'Education Visa (Non-Immigrant ED Visa)', 
     'Passport, Admission Letter, Financial Proof, Health Certificate', 
     60.00, 
     '1-2 weeks', 
     'Course duration', 
     '1. Obtain an admission letter from a Thai institution. 2. Submit the visa application at the Thai embassy or consulate in Taiwan.', 
     'https://www.mfa.go.th/en/services/1065/19386-Visas.html'),

    -- China
    ('China', 'CN', 'X1 Student Visa', 
     'Passport, JW202 Form, Admission Letter, Visa Application Form', 
     75.00, 
     '4-6 weeks', 
     'Course duration + 30 days', 
     '1. Obtain a JW202 Form from the Chinese institution. 2. Submit the visa application at the Chinese embassy or consulate in Taiwan.', 
     'http://cs.mfa.gov.cn/wgrlh/lhqz/lhqzjjs/t960718.shtml'),

    -- Hong Kong
    ('Hong Kong', 'HK', 'Student Visa', 
     'Passport, Admission Letter, Proof of Funds', 
     60.00, 
     '2-3 weeks', 
     'Course duration', 
     '1. Submit the visa application at the Hong Kong Immigration Department. 2. Provide financial proof.', 
     'https://www.immd.gov.hk/eng/services/visas/study.html'),

    -- Canada
    ('Canada', 'CA', 'Study Permit', 
     'Passport, Letter of Acceptance, Proof of Funds, Biometrics', 
     150.00, 
     '4-6 weeks', 
     'Course duration + 90 days', 
     '1. Submit an online application. 2. Provide biometrics. 3. Wait for approval.', 
     'https://www.canada.ca/en/immigration-refugees-citizenship/services/study-canada/study-permit.html');




SELECT * FROM Visa_Requirements;



