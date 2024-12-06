## Command to create a repository using aws cli



**With this command, we create the repository:**

aws ecr create-repository --repository-name clothing-tflite-imagesaws


**And this is the response**


{
    "repository": {
        "repositoryArn": "arn:aws:ecr:us-west-1:487191172021:repository/clothing-tflite-imagesaws",
        "registryId": "487191172021",
        "repositoryName": "clothing-tflite-imagesaws",
        "repositoryUri": "487191172021.dkr.ecr.us-west-1.amazonaws.com/clothing-tflite-imagesaws",
        "createdAt": 1733451899.745,
        "imageTagMutability": "MUTABLE",
        "imageScanningConfiguration": {
            "scanOnPush": false
        },
        "encryptionConfiguration": {
            "encryptionType": "AES256"
        }
    }
}

## Login into the repository

**Now we need to log-in into the repository so we can push our container image for this we use the following command**

$ aws ecr get-login --no-include-email | sed 's/[0-9a-zA-Z=]\{20,\}/PASSWORD/g'

**This will return the result of the command changing the password by the word PASSWORD**

$ aws ecr get-login --no-include-email | sed 's/[0-9a-zA-Z=]\{20,\}/PASSWORD/g'

docker login -u AWS -p PASSWORD https://487191172021.dkr.ecr.us-west-1.amazonaws.com

**The idea of that command was just to show the login instructions we should use. Now we want to submit the result of the actual command into the command line**

**for this we encapsulate the command with $() so the result is input into the prompt**

*$(aws ecr get-login --no-include-email)*

and it confirmed tha login succedded

## Pushing the image

we split the URI information this way

"487191172021.dkr.ecr.us-west-1.amazonaws.com/clothing-tflite-imagesaws"



ACCOUNT=487191172021
REGION=us-west-1
REGISTRY=clothing-tflite-imagesaws
PREFIX=${ACCOUNT}.dkr.ecr.${REGION}.amazonaws.com/${REGISTRY}
TAG=clothing-model-xception-v4-001
REMOTE_URI=${PREFIX}:${TAG}

And we excecute this code on the command line so we have the information 
in memory so we can proceed to next step

## Docker TAG

Now we tag the image we create with this command

$ docker tag clothing-model:latest ${REMOTE_URI}


## Pushing the image

Finally we push the image to the repository

$ docker push ${REMOTE_URI}


