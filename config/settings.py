#run mode
mode = "development"

#define a port for testing
port = 8000

#set static resources path
static_path = '/media/work/python-workspace/Framework/static'

#define a dir for mako to look for templates - relative to the app directory
template_dir = '/media/work/python-workspace/Framework/views'

#define a dir for mako to cache compiled templates
mako_modules_dir = '/media/work/python-workspace/Framework/tmp/views'

#define a database host
db_host = 'localhost'

#define the database port
db_port = 27017

cookie_secret = "61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo="
#should we enable sessions
enable_sessions = True