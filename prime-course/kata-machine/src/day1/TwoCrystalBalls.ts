export default function two_crystal_balls(breaks: boolean[]): number {
    let l = 0;
    let r = breaks.length;

    const n = Math.sqrt(Math.floor(r - l));
    for (let i = 0; i < breaks.length; i += n) {
        if (breaks[i] === true) {
            let lastIdx = i - n + 1;
            do {
                if (breaks[lastIdx] === true) {
                    return lastIdx
                }
                lastIdx += 1;
            } while (lastIdx <= i)
        }
    }
    return -1
}