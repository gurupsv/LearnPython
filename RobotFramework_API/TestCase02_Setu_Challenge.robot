*** Settings ***
Library  RequestsLibrary
Library  JSONLibrary
Library  Collections
Library  PyFunc
Library  json
Library  jwt
Library  OperatingSystem

*** Variables ***
${base_url}  http://localhost:3000
${callbackURL}  http://localhost:3000/api/test
${UserName}  UltraPayer

*** Keywords ***
Create_User
    [Arguments]  ${cburl}  ${uName}
    create session  AddData  ${base_url}
    &{body}=  create dictionary  callbackURL=${cbURL}  name=${uName}
    &{header}=  create dictionary  Content-Type=application/json
    ${response}=  post request  AddData  /api/onboard  data=${body}  headers=${header}
    [Return]    ${response}


*** Test Cases ***
TC_001_Create_New_User
    ${response}=  Create_User  ${callbackURL}  ${UserName}

    ${code}=  convert to string  ${response.status_code}
    log to console  ${response.json()}
    should be equal  ${code}  200


TC_002_Create_User_Without_CallBackURL
    ${response}=  Create_User   ""  ${UserName}

    ${code}=  convert to string  ${response.status_code}
    #log to console  ${response.json()}
    should be equal  ${code}  400

TC003_Create_User_Without_UserName
    ${response}=  Create_User   ${callbackURL}  ""

    ${code}=  convert to string  ${response.status_code}
    #log to console  ${response.json()}
    should be equal  ${code}  400

TC021_Get_Bills_Valid_Creds
    ${response}=  Create_User  ${callbackURL}  ${UserName}
    ${jwtsecret}=  convert to string  ${response.json()['data']['jwtSecret']}
    ${userid}=  convert to string  ${response.json()['data']['id']}

    log to console  "\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
    log to console  ${jwtsecret}
    log to console  ${userid}


    &{payload}=  create dictionary  name=${UserName}
    ${jwttoken}=  getJWT  ${payload}  ${jwtsecret}
    ${jwttoken}=  Catenate  Bearer  ${jwttoken}

    log to console  ${jwttoken}
    log to console  "\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"

    create session  AddData  ${base_url}
    &{header}=  create dictionary  Authorization=${jwttoken}  Content-Type=application/json  payer-id=${userid}
    ${response}=  get request  AddData  /api/bills  headers=${header}

    log to console  ${response.json()['data']['bills']}
    log to console  ${response.status_code}
    ${code}=  convert to string  ${response.status_code}
    should be equal  ${code}  200

TC022_Get_Bills_InValid_Creds
    ${response}=  Create_User  ${callbackURL}  ${UserName}
    ${jwtsecret}=  convert to string  ${response.json()['data']['jwtSecret']}
    ${userid}=  convert to string  ${response.json()['data']['id']}

    log to console  "\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
    log to console  ${jwtsecret}
    log to console  ${userid}
    log to console  "\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"

    &{payload}=  create dictionary  name=${UserName}
    ${jwttoken}=  getJWT  ${payload}  ${jwtsecret}
    ${jwttoken}=  Catenate  Bearer  ${jwttoken}

    create session  AddData  ${base_url}
    &{header}=  create dictionary  Authorization=${jwttoken}  Content-Type=application/json  payer-id="1"
    ${response}=  get request  AddData  /api/bills  headers=${header}

    log to console  ${response.json()}
    log to console  ${response.status_code}
    ${code}=  convert to string  ${response.status_code}
    should be equal  ${code}  403

TC031_Read_Json_File
    ${response}=  Create_User  ${callbackURL}  ${UserName}
    ${jwtsecret}=  convert to string  ${response.json()['data']['jwtSecret']}
    ${userid}=  convert to string  ${response.json()['data']['id']}

    log to console  "\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
    log to console  ${jwtsecret}
    log to console  ${userid}
    log to console  "\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"

    &{payload}=  create dictionary  name=${UserName}
    ${jwttoken}=  getJWT  ${payload}  ${jwtsecret}
    ${jwttoken}=  Catenate  Bearer  ${jwttoken}

    create session  AddData  ${base_url}
    &{header}=  create dictionary  Authorization=${jwttoken}  Content-Type=application/json  payer-id=${userid}
    ${response}=  get request  AddData  /api/bills  headers=${header}

    log to console  ${response.json()}
    log to console  ${response.status_code}
    ${code}=  convert to string  ${response.status_code}
    should be equal  ${code}  200


    ${json}=  get file  6243736135.json
    ${object}=  evaluate  json.loads('''${json}''')  json
    log to console  ${object}