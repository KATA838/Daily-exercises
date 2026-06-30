<?php
    $intArray2 = (2023,6,4,9,33,21,6);
    $sum1 = 0;
    for($i = 0;$i < sizeof($intArry2);$i++)
        {
            echo $intArray2[$i].",";
            $sum1 += $intArray2[$i];
        }
    echo '<br>方法一总和输出为 $sum1<br>';

    $sum1 = 0;
    foreach($intArray2 as $value)
        {
            echo '$value,';
            $sum1 += $value;
        }
    echo '<br>方法二总和输出为 $sum1<br>';
?>
