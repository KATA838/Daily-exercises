<?php
    class CRectAngle
    {
        public $la;//长
        public $lb;//宽
        //构造函数初始化变量
        function __construct($l = 0,$w = 0)
        {
            $this->la = $l;
            $this->lb = $w;
        }
        //面积
        public function getArea()
        {
            return $this->la * $this->lb;
        }
        //周长
        publid function getLength()
        {
            return 2 * ($this->la + $this->lb);
        }
    }
    
    $r1 = new CRectangle(4,3);
    echo '<br>面积 = '.$r1->getArea();
    echo '<br>周长 = '.$r1->getLength();

    $r2 = new CRectangle(8,9);
    echo '<br>面积 = '.$r2->getArea();
    echo '<br>周长 = '.$r2->getLength();
?>