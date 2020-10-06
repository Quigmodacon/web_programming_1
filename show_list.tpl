<html>
    <head>
        <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    </head>
    <body>
        <h3> Todo List, version 1.1</h3>
        <table border="1">
            %for row in rows:
            <tr>
                <td>{{str(row[0])}}</td>
                <td>
                    <a href="/update_item/{{row[0]}}">{{row[1]}}</a>
                </td>
                <td>
                %if row[2]==0:
                    <a href="/set_status/{{row[0]}}/1">[ {{str(row[2])}} ]</a>
                %else :
                    <a href="/set_status/{{row[0]}}/0">[ {{str(row[2])}} ]</a>
                %end
                <td>
                    <a href="/delete_item/{{row[0]}}"><i class="material-icons">delete</i></a>
                </td>
            </tr>
            %end
        </table>
        <hr/>
        <a href="/new_item">New Item... :-)</a>
        <hr/>
        <p> Ankle Biter </p>
    </body>
</html>
