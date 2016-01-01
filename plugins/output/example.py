from honssh import config

from twisted.python import log

class Plugin():

    def __init__(self, cfg):
        self.cfg = cfg

    def start_server(self):
        log.msg('START SERVER')

    def set_server(self, server):
        log.msg('SET SERVER')
    
    def connection_made(self, sensor):
        log.msg(sensor)
    
    def connection_lost(self, sensor):
        log.msg(sensor)
    
    def set_client(self, sensor):
        log.msg(sensor)
    
    def login_successful(self, sensor):
        log.msg(sensor)
    
    def login_failed(self, sensor):
        log.msg(sensor)
    
    def channel_opened(self, sensor):
        log.msg(sensor)
    
    def channel_closed(self, sensor):
        log.msg(sensor)
    
    def command_entered(self, sensor):
        log.msg(sensor)
    
    def download_started(self, sensor):
        log.msg(sensor)

    def download_finished(self, sensor):
        log.msg(sensor)

    def packet_logged(self, sensor):
        log.msg(sensor)
    
    def validate_config(self):
        props = [['example','enabled']]
        for prop in props:
            if not config.checkExist(self.cfg,prop) or not config.checkValidBool(self.cfg, prop):
                return False
        return True
