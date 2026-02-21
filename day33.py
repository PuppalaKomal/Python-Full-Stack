# Testing:
#     why do we perform testing?
#             we perfor testing to the check the logic, conditions and functioning of the project is working as per the requirement or not
#             we can use the keyword assert also we have module pytest
#             for Eg:
#                 def add(x):
#                     return x+1
#                 assert add(3)==4 
#             this test case passes,its a Positive test case 
#             we have to create a folder name Test(root folder) Test_filename
#             Types of test cases:
#                 Positive cases
#                 Negitive cases
#                 Edge cases 
#    Based on Testing Level (SDLC Stages)
            # 1. Unit Testing
                # Tests individual components/functions in isolation
                # Usually done by developers
                # Example: Testing a Python function using unittest or pytest
            # 2. Integration Testing
                # Verifies interaction between modules
                # Example: API + Database integration testing
            # 3. System Testing
                # Tests the complete integrated application
                # Validates end-to-end workflow
            # 4. Acceptance Testing
                # Validates business requirements
                # Types:
                # UAT (User Acceptance Testing)
                # Alpha Testing
                # Beta Testing
#     Based on Testing Technique:
#           Black Box Testing:
#                 No knowledge of internal code
#                 Focus on inputs & outputs
#           White Box Testing:
#                 Tests internal logic, code paths
#                 Tests internal logic, code paths
#                 Includes:
#                 Statement Coverage
#                 Branch Coverage
#                 Path Coverage
#           Grey Box Testing:
#                 Partial knowledge of internal logic
#                 Partial knowledge of internal logic
#     Based on Execution:
#           Manual Testing
#                 Performed by human testers
#                 Automation Testing
#                 Done using tools like:
#                 Selenium
#                 JUnit
#                 TestNG
#                 PyTest
#squre of a number
# def number_squre(x):
#     return x*x

# assert number_squre(2)==4
# print("Working fine")

#check weather the person is eligible to vote or not
def vote_eligibility(age):
    if age>=18:
        return "Eligible to vote"
    else:
        return "Not eligible to vote"
assert vote_eligibility(15)=="Not eligible to vote"
assert vote_eligibility(20)=="Eligible to vote"
assert vote_eligibility(18)=="Eligible to vote"
assert vote_eligibility(17)=="Not eligible to vote"
print ("Working fine")
