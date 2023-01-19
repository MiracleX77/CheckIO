def follow(instructions: str) -> tuple[int, int] | list[int]:
    result=[0,0]
    for i in instructions:
        match i:
            case "f":
                result[1]+=1
            case "b":
                result[1]-=1
            case "l":
                result[0]-=1
            case "r":
                result[0]+=1
    return result
follow("fflff")
