var oracledb = require('oracledb');
var dbConfig = require('./dbConfig');

oracledb.getConnection(
    {
        user: dbConfig.user,
        password: dbConfig.password,
        connectString: dbConfig.connectString
    },
    function (err, connection) {
        if (err) {
            console.error(err.message);
            return;
        }
        connection.execute(
            "SELECT * FROM USERTBL",
            function (err, result) {
                if (err) {
                    console.err(err.message);
                    doRelease(connection);
                    return;
                }
                console.log(result.metaData);
                console.log(result.rows);
                doRelease(connection);
            }
        );
    }
);

function doRelease(connection) {
    connection.release(
        function (err) {
            if (err) {
                console.error(err.message);
            }
        }
    );
}