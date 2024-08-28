from fastapi import status


# code : [message, response http code]
messages = {
    1000: ["User Created Successfully.", status.HTTP_201_CREATED,True],
    1002: ["User Data Not Created.", status.HTTP_400_BAD_REQUEST,False],
    1003: ["Unsuported file type.", status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,False],
    1004: ["Data Fetched Successfully.", status.HTTP_200_OK,True],
    1005: ["Something Went Wrong.", status.HTTP_400_BAD_REQUEST,False],
    1006: ["Data Updated Successfully.", status.HTTP_200_OK,True],
    1007: ["Data Deleted Successfully.", status.HTTP_200_OK,True],
    1008: ["User Data Not Found.", status.HTTP_404_NOT_FOUND,False],
    1009: ["File Already Exists.", status.HTTP_400_BAD_REQUEST,False],
}
