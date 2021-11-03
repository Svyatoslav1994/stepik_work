#mode = 'wsgi'
#working_dir = '/home/box/web'

#bind = "0.0.0.0:8080"
#workers=16
#timeout=60
#pythonpath="/home/box/web"

CONFIG = {                                                                      
    'mode': 'wsgi',                                                           
    'working_dir': '/home/box/web',                                           
    'python': '/usr/bin/python',                                              
    'args': (                                                                   
        '--bind="0.0.0.0:8080"',                                              
        '--workers=16',                                                         
        '--timeout=60',                                                         
        'hello:app',                                                           
    ),                                                                          
}    
