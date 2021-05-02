# Dumplogs
Dumplogs is a python tool for dumping the aws cloudwatch log streams into local files.

## Motivation
On AWS cloud, Users can get historical AWS cloudwatch logs by exporting the log group into S3 bucket. See [AWS logs S3 Export](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/S3Export.html)
The exported file are all in gz format and user need extra efford to download them. 

A more direct approach to dump the logs into local files is to use "aws logs" cli command. But aws-cli logs only allows max. 50 log streams to be retrieved at a time. 
In order to dump the whole logs streams from a log group, user need record the 'next_token' every time by himself.

Dumplogs is inspired by "aws logs" , it aims to dump (and filter) the whole log streams from a AWS log group to local text files. 

## Installation

```bash
pip install https://github.com/xinhuagu/dumplogs.git
```
or
```bash
python3 -m pip install https://github.com/xinhuagu/dumplogs.git
```
## Options



## Usage
Make sure the AWS_PROFILE is set properly
```bash
export AWS_PROFILE=my_profile
```

```bash
usage: dumplogs [-h] [--profile AWS_PROFILE] [-o OUTPUT] group_name
```
- -h --help ``help information``
- -o --output ``output directory, default: current directory``
- --profile ``aws profile, default: AWS_PROFILE env var``
- group_name ``aws log group name``

## Example
```bash
dumplogs /aws/lambda/dpa-kafka-logs -o test --profile DEV
```
or 
```bash
dumplogs /aws/lambda/dpa-kafka-logs
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[Revised BSD License](https://github.com/xinhuagu/dumplogs/blob/master/LICENSE.txt)
