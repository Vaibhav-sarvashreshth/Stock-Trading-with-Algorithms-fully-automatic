from neo_api_client import NeoAPI
import time

def on_message(message):
    print(message)
    
def on_error(error_message):
    print(error_message)

def on_close(message):
    print("on close"+message)
    
def on_open(message):
    print("on open"+message)

#on_message, on_open, on_close and on_error is a call back function we will provide the response for the subscribe method.
# access_token is an optional one. If you have barrier token then pass and consumer_key and consumer_secret will be optional.
# environment by default uat you can pass prod to connect to live server
CK = "N3Mt8S8yWurhevxOUC7L8HsQvdwa"
CS = "dFZGrIDg8hEXkXkOfPfnVus8LDca"
AT = "eyJ4NXQiOiJNbUprWWpVMlpETmpNelpqTURBM05UZ3pObUUxTm1NNU1qTXpNR1kyWm1OaFpHUTFNakE1TmciLCJraWQiOiJaalJqTUdRek9URmhPV1EwTm1WallXWTNZemRtWkdOa1pUUmpaVEUxTlRnMFkyWTBZVEUyTlRCaVlURTRNak5tWkRVeE5qZ3pPVGM0TWpGbFkyWXpOUV9SUzI1NiIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJjbGllbnQ0Nzk4OSIsImF1dCI6IkFQUExJQ0FUSU9OIiwiYXVkIjoiTjNNdDhTOHlXdXJoZXZ4T1VDN0w4SHNRdmR3YSIsIm5iZiI6MTcxNzEzNzAxOCwiYXpwIjoiTjNNdDhTOHlXdXJoZXZ4T1VDN0w4SHNRdmR3YSIsInNjb3BlIjoiZGVmYXVsdCIsImlzcyI6Imh0dHBzOlwvXC9uYXBpLmtvdGFrc2VjdXJpdGllcy5jb206NDQzXC9vYXV0aDJcL3Rva2VuIiwiZXhwIjo5MjIzMzcyMDM2ODU0Nzc1LCJpYXQiOjE3MTcxMzcwMTgsImp0aSI6ImMzMmE3ODUyLTQxYWEtNGY4MS04YWI1LWQxYWI0Njg4OGM1YyJ9.MsYYAkVNC0xCRIh0eL0WgUcbGP0rY9Xu8ufoSjoXwkAKDMNxtktbuXlRw-_5c-LzbrKDFwrh1lVFps_M7f-CWdr_hHyZSmANU8LJhTghY7RB12l2-WcdhiSk81H1I2dr0XlSOu3hD8VH7M5EN_i_8tUIw70DsjXAYa_AiUrnQSr0QJwLbnxKKY0qwZVqKBwN1s5DgEBeIjX3NwL-Uk3xFsOJLk1KoRxEHbFEjutnV6b5aqCuvMIYcqFt62QgPFb0ZSVRNn7SuitLck4AleXs_FAMjxLMAfLWvv40IfgJO6pqA2cc3n7Llu5hVB0OciWGVTBqb8_Pt_tIsuwK4lYN7g"

login_pass = 'RohanPawar@1'
mo_no = "+917058287084"





client = NeoAPI(consumer_key=CK, consumer_secret=CS, environment='prod',
                access_token=AT, neo_fin_key=None)

# # Initiate login by passing any of the combinations mobilenumber & password (or) pan & password (or) userid & password
# # Also this will generate the OTP to complete 2FA
# client.login(mobilenumber=mo_no, password=login_pass)


# time.sleep(60)


    

# lo = client.login(mobilenumber=mo_no,password=login_pass)
# print(lo)
# Get Scrip Master CSV file
client.scrip_master()

# state = client.session_2fa(OTP="8766")

# print(state)








