# amplify-playground

## amplify init
```
? Initialize the project with the above configuration? No
? Enter a name for the environment dev
? Choose your default editor: Visual Studio Code
✔ Choose the type of app that you're building · javascript
Please tell us about your project
? What javascript framework are you using vue
? Source Directory Path:  src
? Distribution Directory Path: dist
? Build Command:  npm run build
? Start Command: npm run dev
Using default provider  awscloudformation
? Select the authentication method you want to use: AWS access keys
? accessKeyId:  ********************
? secretAccessKey:  ****************************************
? region:  us-east-1
```

## amplify add api
```
? Select from one of the below mentioned services: REST
✔ Provide a friendly name for your resource to be used as a label for this category in the project: · v1
✔ Provide a path (e.g., /book/{isbn}): · /api/v1
Only one option for [Choose a Lambda source]. Selecting [Create a new Lambda function].
? Provide an AWS Lambda function name: v1
? Choose the runtime that you want to use: Python
Only one template found - using Hello World by default.

✅ Available advanced settings:
- Resource access permissions
- Scheduled recurring invocation
- Lambda layers configuration
- Environment variables configuration
- Secret values configuration

? Do you want to configure advanced settings? No
? Do you want to edit the local lambda function now? No
```

## amplify update function
```
? Select the Lambda function you want to update v1
General information
- Name: v1
- Runtime: python

Resource access permission
- Not configured

Scheduled recurring invocation
- Not configured

Lambda layers
- arn:aws:lambda:us-east-1:017000801446:layer:AWSLambdaPowertoolsPythonV2:40

Environment variables:
- TZ: Asia/Tokyo

Secrets configuration
- Not configured
```