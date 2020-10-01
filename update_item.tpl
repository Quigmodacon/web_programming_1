<p>Update Task Name</p>
<form action="/update_item" method="POST">
    <input hidden type="text" size="100" maxlength="100" name="id" value="{{str(row[0])}}"/>
    <input type="text" size="100" maxlength="100" name="updated_item" value="{{row[1]}}"/>
    <hr/>
    <input type="submit" name="update_button" value="Update"/>
</form>
</form>        
    <form action="/" method="get" >      
    <input type="submit" name="cancel" value="Cancel"/>      
</form>  
