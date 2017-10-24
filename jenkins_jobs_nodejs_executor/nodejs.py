import xml.etree.ElementTree as XML
from jenkins_jobs.modules.helpers import convert_mapping_to_xml


def nodejs_executor(parser, xml_parent, data):
    """yaml: nodejs
    This plugin allows to execute NodeJS scripts as a job build step.
    Requires the Jenkins :jenkins-wiki:`NodeJS Plugin <NodeJS+Plugin>`.

    :arg str name: NodeJS installation name
    :arg str script: NodeJS script (required)
    :arg str config-id: ID of npmrc config file, which is the
        last field (a 32-digit hexadecimal code) of the path of URL visible
        after you clicked the file under Jenkins Managed Files.
    """

    nodejs = XML.SubElement(xml_parent,
                            'jenkins.plugins.nodejs.NodeJSCommandInterpreter')
    mapping = [('script', 'command', None)]

    mapping_opt = [('name', 'nodeJSInstallationName', None),
                   ('config-id', 'configId', None)]

    convert_mapping_to_xml(nodejs, data, mapping, fail_required=True)
    convert_mapping_to_xml(nodejs, data, mapping_opt, fail_required=False)
