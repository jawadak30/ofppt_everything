<html>
    <head>

    </head>
    <body>
        <?php
            echo "hello php <br/>";
            $color = "green";
            echo "my car is red".$color."<br/>";



            echo "str_replace: ".str_replace(" ","/","hello php")."</br>"
        ?>
        <h1 style="color: <?php echo $color;?>">hello</h>
    </body>
</html>