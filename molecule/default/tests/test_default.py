"""Role testing files using testinfra."""


def test_mysql_running(host):
    mysql = host.service("mysql")
    assert mysql.is_running
    assert mysql.is_enabled

def test_mysql_create_table(host):
    cmd = host.run('mysql -u %s -p%s -h %s -e "CREATE TABLE test_table(id INT);" %s',
                   host.ansible.get_variables()['wp_mysql_user'],
                   host.ansible.get_variables()['wp_mysql_password'],
                   host.ansible.get_variables()['wp_mysql_host'],
                   host.ansible.get_variables()['wp_mysql_db'])
    assert 'ERROR' not in cmd.stderr, "Failed to create table in MySQL"

def test_nginx_installed(host):
    nginx = host.package("nginx")
    assert nginx.is_installed

def test_nginx_running(host):
    nginx = host.service("nginx")
    assert nginx.is_running
    assert nginx.is_enabled

def test_nginx_config(host):
    cmd = host.run("nginx -t")
    assert cmd.rc == 0, "Nginx configuration test failed"

def test_wp_config_exists(host):
    wp_config = host.file("/var/www/html/demo.com/wp-config.php")
    assert wp_config.exists

def test_mysql_connection(host):
    wp_db_host = host.ansible.get_variables().get('wp_db_host')
    wp_db_user = host.ansible.get_variables().get('wp_db_user')
    wp_db_password = host.ansible.get_variables().get('wp_db_password')
    wp_mysql_db = host.ansible.get_variables().get('wp_mysql_db')
    cmd = host.run(f"mysql -h {wp_db_host} -u {wp_db_user} -p{wp_db_password} -e 'SHOW DATABASES;'")
    assert 'Error' not in cmd.stderr, "MySQL connection failed: {}".format(cmd.stderr)
    assert wp_mysql_db in cmd.stdout, "Database {} should be listed in MySQL databases".format(wp_mysql_db)

def test_wordpress_accessible(host):
    response = host.run("curl -sL -w '%{http_code}\\n' 'http://localhost/' -o /dev/null")
    assert response.stdout.strip() == '200', "WordPress is not accessible or not returning HTTP 200"


