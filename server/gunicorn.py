import os
import subprocess

import argparse
import dotenv

import logging
logger = logging.getLogger(__name__)


class Config:
  def __init__(self, mode):
    dotenv.load_dotenv(f'../dot.env.{mode}')

    self.reload_ = bool(int(self.getenv('GUNICORN_RELOAD', True)))
    self.daemon = bool(int(self.getenv('GUNICORN_DAEMON', False)))
    self.host = str(self.getenv('GUNICORN_HOST', '0.0.0.0'))
    self.port = int(self.getenv('GUNICORN_PORT', 5000))
    self.proc_name = str(self.getenv('GUNICORN_PROC_NAME', 'gunicorn'))
    self.workers = int(os.getenv('GUNICORN_WORKERS', 1))
    self.bind = self.host + ':' + str(self.port)
    self.app = str(self.getenv('GUNICORN_APP', 'flask_app:create_app()'))

  def getenv(self, envname, default_val):
    val = os.getenv(envname)
    return val if val else default_val


if __name__ == '__main__':
  try:
    parser = argparse.ArgumentParser(
      description='Launch gunicorn for Flask Webapp.')
    parser.add_argument(
      '--mode', type=str, default='development',
      choices=['development', 'production'])
    args = parser.parse_args()

    config = Config(args.mode)

    cmd = ['gunicorn']
    if config.reload_:
      cmd.extend(['--reload'])
    if config.daemon:
      cmd.extend(['--daemon'])
    cmd.extend(['-b', config.bind])
    cmd.extend(['-n', config.proc_name])
    cmd.extend(['-w', str(config.workers)])
    cmd.extend([f"{config.app}"])

    logger.info(cmd)
    subprocess.run(cmd)
  except KeyboardInterrupt:
    logger.error('Shutdown program by KeyboardInterrupt.')
  except Exception as e:
    logger.error(e)
    exit(-1)
