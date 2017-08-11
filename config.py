import os

def get_env_variable(var_name):
    try:
        return os.environ[var_name]
    except:
        err_msg = "Set the %s environment variable" % var_name
        raise KeyError(err_msg)

username = get_env_variable('USERNAME')
password = get_env_variable('PASSWORD')
client_id = get_env_variable('CLIENT_ID')
client_secret = get_env_variable('CLIENT_SECRET')
user_agent = get_env_variable('USER_AGENT')
