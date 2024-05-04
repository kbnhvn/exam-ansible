"""Role testing files using testinfra."""


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
    wp_config = host.file("/var/www/demo.com/wp-config.php")
    assert wp_config.exists

def test_mysql_connection(host):
    cmd = host.run('php -r \'$mysqli = new mysqli("%s", "%s", "%s", "%s"); if ($mysqli->connect_error) { exit(1); } else { exit(0); }\'', 
                   host.ansible.get_variables()['wp_db_host'],
                   host.ansible.get_variables()['wp_db_user'],
                   host.ansible.get_variables()['wp_db_password'],
                   host.ansible.get_variables()['wp_mysql_db'])
    assert cmd.rc == 0, "MySQL connection test failed"

def test_wordpress_accessible(host):
    response = host.run("curl -sL -w '%{http_code}\\n' 'http://localhost/' -o /dev/null")
    assert response.stdout.strip() == '200', "WordPress is not accessible or not returning HTTP 200"
