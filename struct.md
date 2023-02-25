```
{
    predict_result:JSON,
    recordId:string,
    
}
```



```
[
    ChangeInstrument,
    Rolling,
    Ref,
    Max,
    Min,
    Sum,
    Mean,
    Std,
    Var,
    Skew,
    Kurt,
    Med,
    Mad,
    Slope,
    Rsquare,
    Resi,
    Rank,
    Quantile,
    Count,
    EMA,
    WMA,
    Corr,
    Cov,
    Delta,
    Abs,
    Sign,
    Log,
    Power,
    Add,
    Sub,
    Mul,
    Div,
    Greater,
    Less,
    And,
    Or,
    Not,
    Gt,
    Ge,
    Lt,
    Le,
    Eq,
    Ne,
    Mask,
    IdxMax,
    IdxMin,
    If,
    Feature,
    PFeature,TResample]
```

表达式操作符号
```
ChangeInstrument

变更使用其他的股票的数据：比如说你想要计算 相对于沪深300 的超额收益 
eg: "($close/Ref($close,1) -1) - ChangeInstrument('SH000300', $close/Ref($close,1) -1)"

那么 ($close/Ref($close,1) -1) 这个表达式就是当前行的收益，通过 ChangeInstrument，第一个参数可以接受到你想要使用的股票代码，后面属性中的 Ref 和 $close 就会变成成为对应的股票数据，所以 ChangeInstrument('SH000300', $close/Ref($close,1) -1) 就是 沪深300 的超额收益。

Rolling : TODO


Ref
Parameters
    ----------
    feature : Expression
        feature instance
    N : int
        N = 0, retrieve the first data; N > 0, retrieve data of N periods ago; N < 0, future data

比如: "Ref($close, 60) / $close", 返回过去 60 天的收益率


Max

```