import os

from chalice.cli.factory import CLIFactory
from chalice.utils import UI

API_GATEWAY_STAGE = "api"
CHALICE_STAGE = "dev"

factory = CLIFactory(project_dir=".", environ=os.environ)

config = factory.create_config_obj(
    chalice_stage_name=CHALICE_STAGE,
    autogen_policy=True,
    api_gateway_stage=API_GATEWAY_STAGE
)

session = factory.create_botocore_session()
ui = UI()
d = factory.create_default_deployer(session=session,
                                    config=config,
                                    ui=ui)
deployed_values = d.deploy(config, chalice_stage_name=CHALICE_STAGE)
