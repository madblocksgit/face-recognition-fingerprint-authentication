import boto3



def face_reg(REGION,ACCESS_ID,ACCESS_KEY,source,target):
    # Replace sourceFile and targetFile with the image files you want to compare.
    sourceFile=source
    targetFile=target
    client=boto3.client('rekognition',region_name=REGION,aws_access_key_id=ACCESS_ID,
         aws_secret_access_key= ACCESS_KEY)

    imageSource=open(sourceFile,'rb')
    imageTarget=open(targetFile,'rb')
    try:
     response=client.compare_faces(SimilarityThreshold=70,
                                  SourceImage={'Bytes': imageSource.read()},
                                  TargetImage={'Bytes': imageTarget.read()})
    except:
     #print ("Face not detected, Invalid Image")
     return(0)
    faceMatchFlag=0
    for faceMatch in response['FaceMatches']:
        faceMatchFlag=1
        position = faceMatch['Face']['BoundingBox']
        confidence = str(faceMatch['Face']['Confidence'])
        #print('Face Matched')
    if faceMatchFlag==0:
     #print ('Not Matched')
     return(0)
    else:
        return(1)
    imageSource.close()
    imageTarget.close()

