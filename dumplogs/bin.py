import boto3
import argparse 
import os,sys

def main(argv=None):

    argv = (argv or sys.argv)[1:]
    parser = argparse.ArgumentParser(description='dump all aws log streams into files')
    parser.add_argument("--profile",
                        dest="aws_profile",
                        type=str,
                        default=os.environ.get('AWS_PROFILE', None),
                        help="aws profile")
    parser.add_argument("-o", "--output",
                    type=str,
                    dest='output',
                    default=".",
                    help="output folder")

    parser.add_argument('group_name',help='aws loggroup name')
    options,args = parser.parse_known_args(argv)

    options.aws_profile
    options.output
    options.group_name

    """
    main logic
    """
    client = boto3.client('logs')

    aws_profile = options.aws_profile
    group_name = options.group_name
    output_folder = options.output


    stream_list=[]

    stream_response = client.describe_log_streams(
        logGroupName=group_name,
        orderBy='LastEventTime',
        limit=50,
    )

    while True:
        stream_name_arr = stream_response['logStreams']
        for stream_elm in  stream_name_arr:
            stream_name = stream_elm['logStreamName']
            stream_list.append(stream_name)
        if "nextToken" in stream_response:
            next_token = stream_response['nextToken']

            stream_response = client.describe_log_streams(
                logGroupName=group_name,
                orderBy='LastEventTime',
                nextToken=next_token,
                limit=50,
            )
        else:
            break

    print("loggroup {} has total {} streams".format(group_name,len(stream_list)))

    for s_name in stream_list:
        file_name=s_name.replace("[$LATEST]", "").replace("/","-")
        stream_content= client.get_log_events(
            logGroupName=group_name,
            logStreamName=s_name,
        )
        print("{} ==> {}".format(s_name,file_name))
        completeName = os.path.join(output_folder, file_name)
        with open(completeName, "w") as text_file:
            text_file.write("{}".format(stream_content))

    print("Done.")
