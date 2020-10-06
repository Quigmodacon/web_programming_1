<html>
    <head>
        <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
        <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    </head>
    <body>
        <h3 class="w3-panel w3-center w3-bold w3-indigo"> Todo List, version 1.1</h3>
        <table border="1" class="w3-table-all">
            <tr class="w3-blue">
                <th>EDIT</th>
                <th>TODO</th>
                <th>DONE?</th>
                <th>DELETE</th>
            </tr>    
            %for row in rows:
            <tr class="w3-hoverable w3-hover-green">
                <td>
                    <a href="/update_item/{{row[0]}}"><i class="material-icons">edit</i></a>
                <td>
                    <a>{{row[1]}}</a>
                </td>
                <td>
                %if row[2]==0:
                    <a href="/set_status/{{row[0]}}/1"><i class="material-icons">check_box_outline_blank</i></a>
                %else :
                    <a href="/set_status/{{row[0]}}/0"><i class="material-icons">check_box</i></a>
                %end
                <td>
                    <a href="/delete_item/{{row[0]}}"><i class="material-icons">delete</i></a>
                </td>
            </tr>
            %end
        </table>
        <hr/>
        <div>
            <a href="/new_item"><button class="w3-button w3-red w3-hover-green w3-round">New Item... :-)</button></a>
        </div>
        <hr/>
        <p> Ankle Biter </p>
    </body>
</html>
