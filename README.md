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

## amplify add storage
```
? Select from one of the below mentioned services: NoSQL Database

Welcome to the NoSQL DynamoDB database wizard
This wizard asks you a series of questions to help determine how to set up your NoSQL database table.

✔ Provide a friendly name · v1
✔ Provide table name · v1

You can now add columns to the table.

✔ What would you like to name this column · PK
✔ Choose the data type · string
✔ Would you like to add another column? (Y/n) · yes
✔ What would you like to name this column · SK
✔ Choose the data type · string
✔ Would you like to add another column? (Y/n) · no

Before you create the database, you must specify how items in your table are uniquely organized. You do this by specifying a primary key. The primary key uniquely identifies each item in the table so that no two items can have the same key. This can be an individual column, or a combination that includes a primary key and a sort key.

To learn more about primary keys, see:
https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html#HowItWorks.CoreComponents.PrimaryKey

✔ Choose partition key for the table · PK
✔ Do you want to add a sort key to your table? (Y/n) · yes
Only one option for [Choose sort key for the table]. Selecting [SK].

You can optionally add global secondary indexes for this table. These are useful when you run queries defined in a different column than the primary key.
To learn more about indexes, see:
https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html#HowItWorks.CoreComponents.SecondaryIndexes

✔ Do you want to add global secondary indexes to your table? (Y/n) · no
✔ Do you want to add a Lambda Trigger for your Table? (y/N) · no
```

## amplify update function
```
? Select the Lambda function you want to update v1
General information
- Name: v1
- Runtime: python

Resource access permission
- v1 (create, read, update, delete)

Scheduled recurring invocation
- Not configured

Lambda layers
- arn:aws:lambda:us-east-1:017000801446:layer:AWSLambdaPowertoolsPythonV2:40

Environment variables:
- TZ: Asia/Tokyo

Secrets configuration
- Not configured
```