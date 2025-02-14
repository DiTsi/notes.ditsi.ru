# Python

## PYTHONUNBUFFERED

```dockerfile
FROM python:3.8
ENV PYTHONUNBUFFERED 1
```

> Setting `PYTHONUNBUFFERED=TRUE` or `PYTHONUNBUFFERED=1` (they are equivalent) allows for log messages to be immediately dumped to the stream instead of being buffered. This is useful for receiving timely log messages and avoiding situations where the application crashes without emitting a relevant message due to the message being "stuck" in a buffer.
> 
> As for performance, there can be some (minor) loss that comes with using unbuffered I/O. To mitigate this, I would recommend limiting the number of log messages. If it is a significant concern, one can always leave buffered I/O on and manually flush the buffer when necessary.

from [here](https://github.com/awslabs/amazon-sagemaker-examples/issues/319)