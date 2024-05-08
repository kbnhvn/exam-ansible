"""Role testing files using testinfra."""

def test_mysql_running(host):
    mysql = host.service("mysql")
    assert mysql.is_running
    assert mysql.is_enabled

def test_mysql_create_table(host):
    cmd = host.run('mysql -u %s -p%s -h %s -e "CREATE TABLE test_table(id INT);" %s',
                "datascientest",
                "dbpassword",
                "mysql_instance",  # Point to the MySQL container
                "wordpress")
    assert 'ERROR' not in cmd.stderr, "Failed to create table in MySQL"
