import add from "../instance/example.js";

test("test add function.", () => {
    let n1 = 3, n2 = 4;
    let result = add(n1, n2);

    expect(result).toBe(7);
})

