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

## Usage

```python
import foobar

foobar.pluralize('word') # returns 'words'
foobar.pluralize('goose') # returns 'geese'
foobar.singularize('phenomena') # returns 'phenomenon'
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
