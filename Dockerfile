FROM python:3.9.5
COPY . /
RUN pip install akshare -i https://pypi.tuna.tsinghua.edu.cn/simple/ \
		&& pip install pandas -i https://pypi.tuna.tsinghua.edu.cn/simple/ \
		&& pip install apscheduler -i https://pypi.tuna.tsinghua.edu.cn/simple/
CMD ["python", "-u", "./main.py"]
