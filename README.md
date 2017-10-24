# jenkins-job-builder-nodejs-executor

## NB
This plugin can be useless if this [request](https://review.openstack.org/#/c/514349/) is merged
## Installation
Install it in additional to installed [Jenkins Job Builder](https://github.com/openstack-infra/jenkins-job-builder)
```bash
pip install -e git+git://github.com/vbotay/jenkins-job-builder-nodejs-executor.git#egg=jjb-nodejs-executor
```
Or specify the package in requirements.txt if you install JJB from sources

## Usage
Describe `nodejs` step under `builders` step in job definition.
 * **name**(*optional*) - name of preconfigured NodeJS installation
 * **script**(*mandatory*) - NodeJS script or you can use'!include-raw-escape: some-script.js'
 * **config-id**(*optional*) - ID of npmrc config file, which is the last field (a 32-digit hexadecimal code) of the path of URL visible after you clicked the file under Jenkins Managed Files.

Example:
```yaml
builders:
  - nodejs:
      name: "NodeJS_8.1"
      script: "console.log('Some output');"
      config-id: "e3757442-7c21-4a65-a1ff-6c70f5c6df34"
```
