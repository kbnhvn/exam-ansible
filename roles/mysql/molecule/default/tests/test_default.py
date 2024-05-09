"""Role testing files using testinfra."""

def test_mysql_running(host):
    mysql = host.service("mysql")
    assert mysql.is_running
    assert mysql.is_enabled

def test_mysql_create_database(host):
    cmd = host.run('mysql -u %s -p%s -h %s -e "CREATE DATABASE test_database;"',
                   "datascientest",
                   "dbpassword",
                   "mysql_molecule_instance")  # Point to the MySQL container
    assert 'ERROR' not in cmd.stderr, "Failed to create database in MySQL"
