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
    wp_config = host.file("/var/www/html/demo.com/wp-config.php")
    assert wp_config.exists

