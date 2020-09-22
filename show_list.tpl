<p> Todo List</p>
<table border="1">
    %for row in rows:
    <tr>
        %for item in row:
        <td>{{str(item)}}</td>
        %end
    </tr>
    %end
</table>
<a href="/new_item">New Item...</a>
<hr/>
<a href="/delete_item/5">We don't like number 5</a>