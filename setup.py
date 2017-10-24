from setuptools import setup

setup(
    name='jenkins-job-builder-nodejs-executor',
    version='0.0.1',
    description='Jenkins Job Builder NodeJS script executor',
    url='https://github.com/vbotay/jenkins-job-builder-nodejs-executor.git',
    author='Vasily Gorin',
    author_email='vasilygorin@gmail.com',
    license='MIT license',
    install_requires=[],
    entry_points={
        'jenkins_jobs.builders': [
            'nodejs = jenkins_jobs_nodejs_executor.nodejs:nodejs_executor']},
    packages=['jenkins_jobs_stash_pr'],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3'])
