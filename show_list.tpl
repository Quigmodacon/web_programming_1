<p> Todo List</p>
<table border="1">
    %for row in rows:
    <tr>
        %for item in row[1:]:
        <td>{{str(item)}}</td>
        %end
        <td>
            <a href="/delete_item/{{row[0]}}">delete</a>
        </td>
    </tr>
    %end
</table>
<a href="/new_item">New Item...</a>