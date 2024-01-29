class AbstractBlight:
    blightID = None  # 灾厄的唯一标识符
    name = None  # 灾厄的名称
    description = None  # 灾厄的描述

    unique = None  # 标记灾厄是否独特
    increment = 0  # 灾厄的增量
    floatModAmount = 0.0  # 浮动修改量
    isDone = False  # 标记灾厄是否完成
    isObtained = False  # 标记灾厄是否已获得
    cost = 0  # 灾厄的消耗
    counter = -1  # 灾厄的计数器



    discarded = False  # 标记灾厄是否被丢弃


