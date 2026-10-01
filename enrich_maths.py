import json

def generate_maths_hints():
    with open("maths_questions.json", "r", encoding="utf-8") as f:
        questions = json.load(f)

    # Dictionary of hints and memory tips for each question id (1 to 240)
    # We will build rich, comprehensive, pedagogically sound hints & tips
    hints_tips = {}

    # Define helper to fill
    def add(qid, hint, tip):
        hints_tips[qid] = {"hint": hint, "memory_tip": tip}

    # 1 to 30
    add(1, "The two-digit numbers divisible by 4 range from 12 to 96. Use arithmetic progression: Tn = a + (n-1)d.", 
           "Formula: n = [(Last - First) / d] + 1 = [(96 - 12)/4] + 1 = 21 + 1 = 22.")
    add(2, "Product of two numbers = LCM × HCF. One number is 30, LCM is 120, HCF is 10.", 
           "Product formula: Other number = (LCM × HCF) / Given number = (120 × 10) / 30 = 40.")
    add(3, "A rational number p/q in simplest form has a terminating decimal expansion if q has prime factors of only 2 and/or 5.", 
           "Terminating condition: Denominator in simplest form must be 2^m × 5^n. Here 21/60 = 7/20 = 7/(2^2 × 5).")
    add(4, "Check 6^2 + 7^2 = 36 + 49 = 85. 85 ends in 5, so it is divisible by 5 and not prime.", 
           "Prime check: 85 = 5 × 17, hence composite. Any number ending with 5 (except 5 itself) is composite.")
    add(5, "Find LCM of 4, 6, 8. LCM is 24. Find the smallest three-digit multiple of 24 (greater than or equal to 100).", 
           "LCM(4, 6, 8) = 24. Multiples: 24, 48, 72, 96, 120. Smallest 3-digit multiple is 120.")
    add(6, "Find the highest common factor of 75, 105, and 175. All end in 5: 75=5×15, 105=5×21, 175=5×35. Next common factor: none for 15, 21, 35 together.", 
           "HCF: Prime factors: 75 = 3×5^2, 105 = 3×5×7, 175 = 5^2×7. Common prime power is 5^1 = 5.")
    add(7, "Prime factorize 600: 600 = 6 × 100 = 2 × 3 × 2^2 × 5^2 = 2^3 × 3^1 × 5^2. Number of factors = (p+1)(q+1)(r+1).", 
           "Number of factors formula: (3+1)(1+1)(2+1) = 4 × 2 × 3 = 24.")
    add(8, "1/4 = 0.25 and 1/2 = 0.50. Convert options to decimals or common denominators: 3/7 ≈ 0.428.", 
           "Comparison: 0.25 < 3/7 (0.428) < 0.50. Hence 3/7 lies between 1/4 and 1/2.")
    add(9, "Average = (Sum of all observations) / (Total number of observations) = (4.2 + 3.8 + 7.6) / 3.", 
           "Calculation: 4.2 + 3.8 + 7.6 = 15.6. Average = 15.6 / 3 = 5.2.")
    add(10, "Half of a number means dividing it by 2: 0.1 / 2 = 1 / 20 = 0.05.", 
           "Memory tip: 0.10 / 2 = 0.05. Avoid confusing 0.5 with 0.05!")
    add(11, "Find LCM of 20, 25, 30: 20=2^2×5, 25=5^2, 30=2×3×5. Highest powers: 2^2 × 3^1 × 5^2.", 
           "LCM = 4 × 3 × 25 = 300.")
    add(12, "Two numbers are co-prime if their HCF is 1. Any two consecutive integers are always co-prime.", 
           "Co-prime rule: HCF(n, n+1) = 1. Since 215 and 216 are consecutive, they are co-prime.")
    add(13, "If a number has n digits, its square has either 2n - 1 or 2n digits. Here n = 5.", 
           "Square digits rule: For n-digit number, digits in square = (2n - 1) or 2n. For n=5: 9 or 10 digits.")
    add(14, "Sum of first n odd positive integers is n^2. Here sum is 144, so n^2 = 144.", 
           "Formula: 1 + 3 + 5 + ... + (2n-1) = n^2. Given sum = 144 => n = √144 = 12.")
    add(15, "Three-digit numbers range from 100 to 999. √100 = 10, √999 ≈ 31.62. Squares go from 10^2 to 31^2.", 
           "Total perfect squares = 31 - 10 + 1 = 22 perfect squares.")
    add(16, "Check the prime factorization or square root. 2744 = 14^3 = 2^3 × 7^3, which is a perfect cube, not a square.", 
           "Memory tip: 2744 = 14^3. The powers of prime factors must be even for a perfect square.")
    add(17, "Use identity: a^3 + b^3 = (a + b)(a^2 - ab + b^2). The denominator matches (a^2 - ab + b^2).", 
           "Identity: (a^3 + b^3) / (a^2 - ab + b^2) = a + b = 3.2 + 1.8 = 5.")
    add(18, "Smallest number divisible by 6, 9, 15 is their LCM = 90 = 2 × 3^2 × 5. To make it a square, multiply by 2 × 5.", 
           "Smallest square = 90 × 10 = 900. (30^2 = 900).")
    add(19, "Cube root of 3375: Since it ends in 5, the unit digit is 5. 1^3=1, 2^3=8, so tens digit is 1.", 
           "Cube root: 15^3 = 3375, so 3√3375 = 15.")
    add(20, "Expand (100 + 1)^3 using (a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3.", 
           "Expansion: 1000000 + 3(10000) + 3(100) + 1 = 1030301.")
    add(21, "Use pattern identity: n^3 - (n-1)^3 = 1 + n(n-1)×3.", 
           "Identity: 7^3 - 6^3 = 1 + 7 × 6 × 3 = 1 + 126 = 127.")
    add(22, "Unit digit of 8^3 = 8 × 8 × 8 = 512, which ends in 2.", 
           "Unit digit cyclicity for 8: 8^1=8, 8^2=4, 8^3=2, 8^4=6. So unit digit of 888^3 is 2.")
    add(23, "Square root of 13225: Ends in 25, so last digit is 5. 11 × 12 = 132, so tens digits are 11.", 
           "Shortcut: For numbers ending in 25, √13225: 11 × 12 = 132, so answer is 115.")
    add(24, "Use (a + b)^2 = a^2 + 2ab + b^2 with a = 10000, b = 1.", 
           "Square calculation: 10001^2 = (10000 + 1)^2 = 100000000 + 20000 + 1 = 100020001.")
    add(25, "Simplify: (3^5 - 3^3) / ... or factor 3^3(3^2 - 1) = 27 × 8.", 
           "Exponent rules: a^m / a^n = a^(m-n). Simplify the expression systematically to get 9.")
    add(26, "Apply laws of exponents: combine base powers 2 and 3.", 
           "Laws of Indices: a^m × a^n = a^(m+n), (a^m)^n = a^(mn). Simplifying gives 36.")
    add(27, "Standard scientific notation has 1 digit before decimal: 384,000,000 m = 3.84 × 10^8 m.", 
           "Scientific notation: M × 10^n where 1 ≤ M < 10. Distance = 3.84 × 10^8 meters.")
    add(28, "0.00001275m in scientific notation: Move decimal 5 places to the right to get 1.275.", 
           "Scientific notation: 0.00001275 = 1.275 × 10^-5.")
    add(29, "Any non-zero expression raised to power 0 equals 1: a^0 = 1.", 
           "Zero exponent rule: (any non-zero quantity)^0 = 1.")
    add(30, "(-3)^(m-1) × (-3)^6 = (-3)^(m-1+6) = (-3)^(m+5). Since (-3)^(m+5) = (-3)^7, m + 5 = 7.", 
           "Equating exponents: m + 5 = 7 => m = 2.")

    # 31 to 60: Ratios, Proportions, Percentages, Interest, Work
    add(31, "Apply direct or inverse proportion based on the situation.", "Direct: x1/y1 = x2/y2; Inverse: x1*y1 = x2*y2.")
    add(32, "Simplify ratios by dividing terms by their common factors.", "Ratio in simplest form: a:b = (a/gcd):(b/gcd).")
    add(33, "Find the percentage increase or decrease = (Difference / Original) × 100%.", "% Change = (Change / Original) × 100.")
    add(34, "Simple Interest formula: SI = (P × T × R) / 100.", "SI = PTR / 100; Amount = P + SI.")
    add(35, "Compound interest amount: A = P(1 + R/100)^n.", "CI = A - P = P[(1 + R/100)^n - 1].")
    add(36, "Profit percentage = (Profit / Cost Price) × 100%.", "Profit = SP - CP; Profit % = (Profit/CP) × 100.")
    add(37, "Loss percentage = (Loss / Cost Price) × 100%.", "Loss = CP - SP; Loss % = (Loss/CP) × 100.")
    add(38, "Discount is always calculated on the Marked Price (MP).", "SP = MP - Discount; Discount % = (Discount / MP) × 100.")
    add(39, "Work done = Rate × Time. If A completes work in x days, 1 day work = 1/x.", "Combined 1-day work = (1/A + 1/B); Total days = (AB)/(A+B).")
    add(40, "Speed = Distance / Time. To convert km/h to m/s, multiply by 5/18.", "Conversion: 1 km/h = 5/18 m/s; 1 m/s = 18/5 km/h.")
    add(41, "Two ratios a:b and c:d are in proportion if product of extremes = product of means (ad = bc).", "Proportion property: a/b = c/d <=> a × d = b × c.")
    add(42, "Check equality of cross-products to verify proportion.", "For a:b :: c:d, verify ad = bc.")
    add(43, "Use unitary method: find the value of one unit first, then multiply by required quantity.", "Unitary rule: Value of n units = (Value of 1 unit) × n.")
    add(44, "Express fraction as percentage by multiplying with 100.", "Fraction to %: Multiply by 100. % to Fraction: Divide by 100.")
    add(45, "Successive discounts d1 and d2 have effective discount = (d1 + d2 - d1*d2/100)%.", "Net discount formula = d1 + d2 - (d1 × d2)/100.")
    add(46, "Find Cost Price when SP and Profit% are given: CP = (SP × 100) / (100 + P%).", "CP formula: CP = SP × 100 / (100 + Profit%).")
    add(47, "Calculate time taken in hours, minutes, and seconds using Distance / Speed.", "Time = Distance / Relative Speed.")
    add(48, "Ratio of areas of similar figures is the square of the ratio of their corresponding sides.", "Area ratio = (side1 / side2)^2.")
    add(49, "When money doubles in T years at simple interest, R = 100 / T.", "Doubling rule (SI): R × T = 100.")
    add(50, "Difference between CI and SI for 2 years = P(R/100)^2.", "Diff(2 yrs) = P × (R/100)^2.")
    add(51, "Average speed for equal distances covered at speeds x and y is 2xy / (x + y).", "Harmonic Mean formula: Avg Speed = 2xy / (x + y).")
    add(52, "Relative speed when moving in opposite directions = S1 + S2; same direction = |S1 - S2|.", "Opposite: add speeds; Same direction: subtract speeds.")
    add(53, "Time taken by train of length L to cross a pole = L / Speed.", "Train crossing pole: Distance = Length of train.")
    add(54, "Time taken by train of length L to cross platform of length P = (L + P) / Speed.", "Train crossing platform: Total distance = L + P.")
    add(55, "Pipes and Cisterns: Net rate per hour = 1/Inlet - 1/Outlet.", "Net filling rate = (1/x - 1/y) per hour.")
    add(56, "Alloy mixture: Use weighted averages or alligation rule.", "Alligation rule: (Cheaper / Dearer) = (d - m) / (m - c).")
    add(57, "Find the unknown term x in the proportion a : b :: c : x => x = (b × c) / a.", "Fourth proportional: x = (b × c) / a.")
    add(58, "Mean proportional between a and b is √(ab).", "Mean proportional formula: b = √(ac).")
    add(59, "Third proportional to a and b is b^2 / a.", "Third proportional: c = b^2 / a.")
    add(60, "Sum of ratio parts: Divide total quantity by sum of ratio parts.", "Part value = (Total / Sum of parts) × individual ratio.")

    # 61 to 100: Geometry
    add(61, "A line segment has two fixed end points.", "Line segment: 2 end points, fixed length. Ray: 1 end point. Line: 0 end points.")
    add(62, "A ray has exactly one starting endpoint and extends infinitely in one direction.", "Ray: 1 endpoint, indefinite length.")
    add(63, "Complementary angles add up to 90 degrees.", "Complementary: A + B = 90°; Supplementary: A + B = 180°.")
    add(64, "Supplementary angles add up to 180 degrees.", "Supplementary angles: sum = 180° (linear pair).")
    add(65, "Vertically opposite angles are always equal.", "When two lines intersect, opposite angles are equal.")
    add(66, "Sum of interior angles of a triangle is always 180°.", "Angle sum property of triangle: ∠A + ∠B + ∠C = 180°.")
    add(67, "An exterior angle of a triangle equals the sum of its two interior opposite angles.", "Exterior angle theorem: Ext ∠ = Int ∠1 + Int ∠2.")
    add(68, "Sum of interior angles of an n-sided polygon is (n - 2) × 180°.", "Formula: Total interior angle sum = (n - 2) × 180°.")
    add(69, "Each interior angle of a regular polygon with n sides is [(n - 2) × 180°] / n.", "Regular polygon interior angle: [(n - 2) × 180°] / n.")
    add(70, "Sum of exterior angles of any polygon is always 360°.", "Exterior angle sum = 360° for any convex polygon.")
    add(71, "Number of diagonals in an n-sided polygon is n(n - 3) / 2.", "Diagonals formula: d = n(n - 3) / 2.")
    add(72, "In a right-angled triangle, hypotenuse^2 = base^2 + height^2 (Pythagoras Theorem).", "Pythagoras theorem: c^2 = a^2 + b^2.")
    add(73, "Equilateral triangle has all 3 sides equal and each angle measures 60°.", "Equilateral triangle: All sides equal, each angle = 60°.")
    add(74, "Isosceles triangle has two equal sides and angles opposite to equal sides are equal.", "Isosceles triangle: 2 equal sides, base angles equal.")
    add(75, "Median connects a vertex to the midpoint of the opposite side.", "Medians intersect at Centroid (G), dividing each median in ratio 2:1.")
    add(76, "Altitude is a perpendicular drawn from a vertex to the opposite side.", "Altitudes intersect at the Orthocenter (H).")
    add(77, "Perpendicular bisectors of sides meet at the Circumcenter (S).", "Circumcenter is equidistant from all three vertices.")
    add(78, "Angle bisectors meet at the Incenter (I).", "Incenter is equidistant from all three sides.")
    add(79, "Sum of any two sides of a triangle must be strictly greater than the third side.", "Triangle inequality theorem: a + b > c, b + c > a, c + a > b.")
    add(80, "Difference of any two sides of a triangle is always less than the third side.", "Side difference rule: |a - b| < c.")
    add(81, "In a cyclic quadrilateral, opposite angles are supplementary (add to 180°).", "Cyclic quadrilateral: ∠A + ∠C = 180°, ∠B + ∠D = 180°. If ∠A = 50°, ∠C = 130°.")
    add(82, "Angle in a semicircle is a right angle (90°).", "Thales's theorem: Angle inscribed in a semicircle = 90°.")
    add(83, "Angles in the same segment of a circle are equal.", "Inscribed angle property: Angles subtended by same arc at circumference are equal.")
    add(84, "Angle subtended by an arc at the center is double the angle subtended at the circumference.", "Central angle theorem: ∠Center = 2 × ∠Circumference.")
    add(85, "A tangent to a circle is perpendicular to the radius at the point of contact.", "Tangent-Radius property: Tangent ⊥ Radius (angle = 90°).")
    add(86, "Lengths of tangents drawn from an external point to a circle are equal.", "External tangents theorem: PA = PB.")
    add(87, "Sum of opposite pairs of sides of a circumscribing quadrilateral are equal.", "AB + CD = AD + BC for circumscribed quadrilateral.")
    add(88, "A quadrilateral with opposite sides parallel and equal is a parallelogram.", "Parallelogram: Opp sides parallel & equal, opp angles equal, diagonals bisect each other.")
    add(89, "In a rhombus, diagonals bisect each other at right angles (90°).", "Rhombus: All sides equal, diagonals perpendicular bisectors.")
    add(90, "In a rectangle, diagonals are equal and bisect each other.", "Rectangle: Opposite sides equal, each angle 90°, diagonals equal.")
    add(91, "In a square, all sides are equal, all angles 90°, diagonals equal and perpendicular bisectors.", "Square: Combines all properties of rectangle and rhombus.")
    add(92, "Trapezium is a quadrilateral with at least one pair of parallel sides.", "Area of trapezium = 1/2 × (a + b) × h.")
    add(93, "Kite has two pairs of equal adjacent sides; diagonals are perpendicular.", "Kite area = 1/2 × d1 × d2.")
    add(94, "Criteria for congruence of triangles: SSS, SAS, ASA, AAS, RHS. (AAA is similarity, NOT congruence).", "Congruence: SSS, SAS, ASA, AAS, RHS. Note: AAA gives similar triangles, not congruent.")
    add(95, "Basic Proportionality Theorem (Thales Theorem): If a line is drawn parallel to one side of a triangle, it divides the other two sides proportionally.", "BPT: AD/DB = AE/EC when DE || BC.")
    add(96, "Ratio of areas of two similar triangles is equal to the square of the ratio of their corresponding sides.", "Ar(T1)/Ar(T2) = (s1/s2)^2 = (h1/h2)^2 = (m1/m2)^2.")
    add(97, "Pythagorean triplet check: a^2 + b^2 = c^2 (e.g., 3-4-5, 5-12-13, 7-24-25, 8-15-17).", "Common triplets: (3,4,5), (5,12,13), (7,24,25), (8,15,17), (9,40,41).")
    add(98, "Euler's formula for polyhedra: V - E + F = 2, where V=Vertices, E=Edges, F=Faces.", "Euler's formula: Faces + Vertices - Edges = 2 (F + V = E + 2).")
    add(99, "A regular polyhedron (Platonic solid) has identical regular polygon faces meeting at each vertex. There are exactly 5.", "5 Platonic solids: Tetrahedron, Cube (Hexahedron), Octahedron, Dodecahedron, Icosahedron.")
    add(100, "Reflex angle is an angle greater than 180° and less than 360°.", "Angle types: Acute (<90°), Right (90°), Obtuse (90°-180°), Straight (180°), Reflex (180°-360°).")

    # 101 to 140: Algebra & Number patterns
    add(101, "Factorize x^2 - 3x - 10 = 0: (x - 5)(x + 2) = 0, so roots are 5 and -2.", "Factoring: Sum = -3, Product = -10. Numbers are -5 and 2. Roots: x = 5, -2.")
    add(102, "Discriminant of ax^2 + bx + c = 0 is D = b^2 - 4ac. Nature of roots depends on sign of D.", "D > 0: real & distinct; D = 0: real & equal; D < 0: complex/imaginary.")
    add(103, "Sum of roots = -b/a, Product of roots = c/a.", "Quadratic relations: α + β = -b/a, αβ = c/a.")
    add(104, "In an Arithmetic Progression (AP), nth term Tn = a + (n - 1)d.", "AP nth term: an = a + (n - 1)d.")
    add(105, "Sum of first n terms of an AP: Sn = n/2 [2a + (n - 1)d] = n/2 [a + l].", "AP sum formula: Sn = n(a + l)/2.")
    add(106, "In a Geometric Progression (GP), nth term Tn = a * r^(n - 1).", "GP nth term: an = ar^(n-1).")
    add(107, "Sum of first n terms of GP: Sn = a(r^n - 1)/(r - 1) for r > 1.", "GP sum: Sn = a(1 - r^n)/(1 - r) for r < 1.")
    add(108, "Sum to infinity of a GP with |r| < 1 is S∞ = a / (1 - r).", "Infinite GP sum: S = a / (1 - r).")
    add(109, "For linear system a1*x + b1*y + c1 = 0 and a2*x + b2*y + c2 = 0, unique solution if a1/a2 ≠ b1/b2.", "Lines intersect: a1/a2 ≠ b1/b2 (Consistent, unique solution).")
    add(110, "Infinitely many solutions (coincident lines) if a1/a2 = b1/b2 = c1/c2.", "Coincident lines: a1/a2 = b1/b2 = c1/c2 (Dependent, infinite solutions).")
    add(111, "No solution (parallel lines) if a1/a2 = b1/b2 ≠ c1/c2.", "Parallel lines: a1/a2 = b1/b2 ≠ c1/c2 (Inconsistent, no solution).")
    add(112, "Degree of a non-zero constant polynomial is 0. Degree of zero polynomial is not defined.", "Constant polynomial degree = 0; Linear = 1; Quadratic = 2; Cubic = 3.")
    add(113, "Remainder Theorem: When polynomial p(x) is divided by (x - a), remainder is p(a).", "Remainder = p(a). Factor theorem: (x - a) is a factor if p(a) = 0.")
    add(114, "Use identity: (a + b + c)^2 = a^2 + b^2 + c^2 + 2ab + 2bc + 2ca.", "Trinomial square expansion: (a+b+c)^2 = ∑a^2 + 2∑ab.")
    add(115, "If a + b + c = 0, then a^3 + b^3 + c^3 = 3abc.", "Conditional identity: a + b + c = 0 => a^3 + b^3 + c^3 = 3abc.")
    add(116, "Degree of product of polynomials = deg(p) + deg(q).", "Degree rule: deg(P × Q) = deg(P) + deg(Q).")
    add(117, "Substitute coordinates to check if a point lies on the line ax + by + c = 0.", "Point satisfies equation: LHS = RHS.")
    add(118, "Solve system by substitution, elimination, or cross-multiplication method.", "Elimination: Multiply equations to match coefficients, then add/subtract.")
    add(119, "Common difference of AP: d = a_(k+1) - a_k.", "d = Tn - T_(n-1). AP is constant if d=0, increasing if d>0, decreasing if d<0.")
    add(120, "Arithmetic Mean (AM) between a and b is (a + b) / 2.", "AM = (a + b)/2; Geometric Mean (GM) = √(ab); Harmonic Mean (HM) = 2ab/(a+b).")
    add(121, "Path inside a rectangle: Inner dimensions = (L - 2w) and (B - 2w). Area of path = Outer Area - Inner Area.", "Area of path = LB - (L - 2w)(B - 2w) = 2w(L + B - 2w).")
    add(122, "Path outside a rectangle: Outer dimensions = (L + 2w) and (B + 2w). Area = 2w(L + B + 2w).", "Outer path area = (L + 2w)(B + 2w) - LB = 2w(L + B + 2w).")
    add(123, "Two central crossroads of width w: Area = w(L + B - w).", "Crossroads area = wL + wB - w^2 = w(L + B - w).")
    add(124, "Area of triangle using Heron's formula: √[s(s - a)(s - b)(s - c)], where s = (a + b + c)/2.", "Heron's formula: Δ = √[s(s-a)(s-b)(s-c)], semi-perimeter s = (a+b+c)/2.")
    add(125, "Area of equilateral triangle = (√3 / 4) * side^2. Height = (√3 / 2) * side.", "Equilateral triangle: Area = (√3/4)a^2, Altitude = (√3/2)a.")
    add(126, "Area of parallelogram = Base × Height.", "Parallelogram area = b × h = ab sin θ.")
    add(127, "Area of rhombus = 1/2 × d1 × d2.", "Rhombus area = half of product of diagonals.")
    add(128, "Area of circle = πr^2; Circumference = 2πr.", "Circle: A = πr^2 = πd^2/4, C = 2πr = πd.")
    add(129, "Area of sector = (θ / 360°) × πr^2. Length of arc = (θ / 360°) × 2πr.", "Sector area = (θ/360)πr^2 = 1/2 × l × r.")
    add(130, "Perimeter of semi-circle = πr + 2r = r(π + 2) ≈ 36r/7.", "Semi-circle perimeter = πr + 2r = r(22/7 + 2) = 36r/7.")
    add(131, "Total surface area of cuboid = 2(lb + bh + hl); Volume = l × b × h.", "Cuboid: TSA = 2(lb+bh+hl), LSA = 2h(l+b), Vol = lbh.")
    add(132, "Diagonal of a cuboid = √(l^2 + b^2 + h^2). Diagonal of cube = a√3.", "Longest rod in a room = √(l^2 + b^2 + h^2).")
    add(133, "Volume of cube = a^3; Total surface area = 6a^2; Lateral surface area = 4a^2.", "Cube: Vol = a^3, TSA = 6a^2, LSA = 4a^2.")
    add(134, "Curved surface area of cylinder = 2πrh; Total surface area = 2πr(r + h).", "Cylinder: CSA = 2πrh, TSA = 2πr(h + r), Vol = πr^2h.")
    add(135, "Volume of right circular cylinder = πr^2h.", "Cylinder Volume = Base area × Height = πr^2h.")
    add(136, "Slant height of cone: l = √(r^2 + h^2).", "Cone: l = √(r^2 + h^2), CSA = πrl, TSA = πr(l + r), Vol = 1/3 πr^2h.")
    add(137, "Curved surface area of cone = πrl; Volume = 1/3 πr^2h.", "Volume of cone is 1/3 of cylinder with same base and height.")
    add(138, "Surface area of sphere = 4πr^2; Volume = 4/3 πr^3.", "Sphere: Surface Area = 4πr^2, Volume = 4/3 πr^3.")
    add(139, "Hemisphere: Curved surface area = 2πr^2; Total surface area = 3πr^2; Volume = 2/3 πr^3.", "Hemisphere: CSA = 2πr^2, TSA = 3πr^2, Vol = 2/3 πr^3.")
    add(140, "When a solid is recast into another shape, the volume remains conserved.", "Conservation of volume: Volume of original solid = Volume of new solid(s).")

    # 141 to 180: Mensuration, Probability, Coordinate Geometry, Trigonometry
    add(141, "Given height h = 21 cm, slant height l. Find radius r = √(l^2 - h^2).", "Cone relation: r = √(l^2 - h^2).")
    add(142, "Find volume or surface area using standard formulas.", "Surface Area / Volume application.")
    add(143, "Displacement by sphere = Volume of sphere = 4/3 πr^3.", "Archimedes principle: Water displaced = volume of submerged body.")
    add(144, "Total surface area of cone = Curved Surface Area + Base Area = πrl + πr^2.", "TSA of cone = πrl + πr^2 = πr(l + r).")
    add(145, "Sum of probabilities of all elementary events of an experiment is always equal to 1.", "P(E1) + P(E2) + ... + P(En) = 1.")
    add(146, "Probability of a sure / certain event is 1.", "Certain event: P(E) = 1. Probability range: 0 ≤ P(E) ≤ 1.")
    add(147, "Probability of an impossible event is 0.", "Impossible event: P(E) = 0.")
    add(148, "Deck of 52 cards contains 4 kings. P(King) = 4 / 52 = 1 / 13.", "P(King) = Number of kings / Total cards = 4/52 = 1/13.")
    add(149, "Face cards are King, Queen, Jack (3 per suit × 4 suits = 12 cards). P(Face) = 12 / 52 = 3 / 13.", "Face cards: 12 cards. P = 12/52 = 3/13.")
    add(150, "A standard die has numbers {1, 2, 3, 4, 5, 6}. Even numbers: {2, 4, 6} (3 outcomes). P(Even) = 3 / 6 = 1 / 2.", "P(Even) = 3/6 = 1/2.")
    add(151, "Probability = Number of favorable outcomes / Total possible outcomes.", "P(E) = n(E) / n(S).")
    add(152, "P(winning) + P(losing) = 1. If P(losing) is 0.35, P(winning) = 1 - 0.35 = 0.65.", "Complementary event: P(A) + P(not A) = 1.")
    add(153, "In a normal year (365 days), probability of a specific event occurring on an exact day.", "Normal year: 365 days. Probability = 1/365.")
    add(154, "When two dice are thrown, total outcomes = 36. Doublets: (1,1), (2,2), (3,3), (4,4), (5,5), (6,6) = 6 outcomes. P = 6/36 = 1/6.", "Doublets on two dice: 6/36 = 1/6.")
    add(155, "When two coins are tossed, outcomes: {HH, HT, TH, TT}. At least one head: {HH, HT, TH} (3 outcomes). P = 3/4 = 0.75.", "At least one head = 1 - P(no head) = 1 - 1/4 = 3/4 = 0.75.")
    add(156, "Tossing a single fair coin has 2 outcomes {H, T}. P(Head) = 1 / 2.", "Coin toss: P(Head) = 1/2 = 0.5.")
    add(157, "Points of trisection divide the segment in ratios 1:2 and 2:1 using section formula.", "Section formula: [(m1*x2 + m2*x1)/(m1+m2), (m1*y2 + m2*y1)/(m1+m2)].")
    add(158, "Distance formula: d = √[(x2 - x1)^2 + (y2 - y1)^2]. Equate distances and simplify.", "Equidistant point condition: PA = PB <=> PA^2 = PB^2. Gives x - y = 2.")
    add(159, "Distance between (x1, y) and (x2, y) on horizontal line = |x2 - x1| = |8 - 4| = 4.", "Distance along parallel to x-axis = |x2 - x1|.")
    add(160, "Collinear points lie on the same straight line, so area of triangle formed by them is 0.", "Collinear condition: Area of triangle = 0.")
    add(161, "Use distance formula √[(x - 1)^2 + (7 - 15)^2] = d. Solve for x.", "Distance formula: (x - 1)^2 + (-8)^2 = d^2.")
    add(162, "Centroid formula: G = [(x1 + x2 + x3)/3, (y1 + y2 + y3)/3]. (-4+2+2)/3 = 0/3 = 0; (6-2+5)/3 = 9/3 = 3.", "Centroid G = (∑x/3, ∑y/3) = (0, 3).")
    add(163, "Distance from origin (0,0) to (x, y) is √(x^2 + y^2) = √(7^2 + 4^2) = √(49 + 16) = √65.", "Distance from origin = √(x^2 + y^2) = √65.")
    add(164, "Apply section formula for internal division.", "Section formula: x = (mx2 + nx1)/(m+n), y = (my2 + ny1)/(m+n).")
    add(165, "The centroid of a triangle divides each median in the ratio 2 : 1 from the vertex.", "Centroid ratio: Vertex to Centroid : Centroid to Midpoint = 2 : 1.")
    add(166, "Radius = Distance from center to any point on circle. Use distance formula.", "Radius r = √[(x2-x1)^2 + (y2-y1)^2].")
    add(167, "Midpoint formula: M = [(x1 + x2)/2, (y1 + y2)/2].", "Midpoint M = ((x1+x2)/2, (y1+y2)/2).")
    add(168, "In a parallelogram, diagonals bisect each other: Midpoint of AC = Midpoint of BD.", "Parallelogram diagonal property: Midpoint(AC) = Midpoint(BD). Equate x and y coordinates.")
    add(169, "The concept of 'ardha-jya' or 'jya' (sine) was introduced by Aryabhata in Aryabhatiya (499 AD).", "Historical fact: Aryabhata introduced 'jya' which translated through Arabic into Latin 'sinus' (sine).")
    add(170, "If tan A = 4/3, opposite = 4, adjacent = 3 => hypotenuse = √(4^2 + 3^2) = 5. sin A = opp/hyp = 4/5.", "Pythagorean triplet (3, 4, 5): tan A = 4/3 => sin A = 4/5, cos A = 3/5.")
    add(171, "AB = 24, BC = 7 => AC = √(24^2 + 7^2) = √(576 + 49) = √625 = 25. sin C = opp/hyp = AB/AC or BC/AC depending on angle.", "Right triangle (7, 24, 25): sin θ = opposite / hypotenuse = 7/25.")
    add(172, "sin 45° = 1/√2, cos 45° = 1/√2. sin 45° + cos 45° = 1/√2 + 1/√2 = 2/√2 = √2.", "Values: sin 45° = cos 45° = 1/√2. Sum = 2/√2 = √2.")
    add(173, "2 tan 30° / (1 + tan^2 30°) = sin(2 × 30°) = sin 60°.", "Trigonometric identity: sin 2θ = 2 tan θ / (1 + tan^2 θ).")
    add(174, "Use angle sum or difference formula: sin(A - B) value to find angle.", "Standard trig values: sin 30° = 1/2, sin 45° = 1/√2, sin 60° = √3/2, sin 90° = 1.")
    add(175, "Recall fundamental identity: sec^2 θ - tan^2 θ = 1. Therefore, tan^2 θ - sec^2 θ = -1.", "Identity: 1 + tan^2 θ = sec^2 θ => tan^2 θ - sec^2 θ = -1.")
    add(176, "Evaluate the trigonometric expression using standard triangle ratios.", "Trig evaluation: substitute values of sin, cos, or tan for 45°.")
    add(177, "tan A × cot A = 1, and cos A × sec A = 1. Both equal 1.", "Reciprocal relations: tan A = 1/cot A, cos A = 1/sec A, sin A = 1/cosec A.")
    add(178, "sin 2A = 2 sin A cos A. For this to equal 2 sin A, cos A must equal 1, which happens at A = 0°.", "When A = 0°: sin(0) = 0 and 2 sin(0) = 0.")
    add(179, "In a right triangle, tan A = Opposite side / Adjacent side.", "SOH-CAH-TOA: tan θ = Opposite / Adjacent.")
    add(180, "Use identity: sin A cos B + cos A sin B = sin(A + B) = sin(60° + 30°) = sin 90° = 1.", "Compound angle formula: sin(A + B) = sin A cos B + cos A sin B. sin 90° = 1.")

    # 181 to 200: Heights, Distances & Definitions
    add(181, "If height of person = length of shadow (h = s), then tan θ = h / s = 1 => θ = 45°.", "When height = shadow: tan θ = 1 => Angle of elevation θ = 45°.")
    add(182, "Length of shadow = √3 × height. tan θ = height / shadow = h / (h√3) = 1/√3 => θ = 30°.", "tan θ = 1/√3 => Angle of elevation = 30°.")
    add(183, "tan θ = Height / Base. Given distance and angle, find height = distance × tan θ.", "Height = Base × tan θ. For 30°: H = d × (1/√3); for 60°: H = d × √3.")
    add(184, "The trigonometric ratio relating height (opposite) and shadow (adjacent) is tan θ.", "tan θ = Opposite (height) / Adjacent (shadow).")
    add(185, "Use right triangle trigonometry to calculate the required height.", "tan θ = flag height / distance.")
    add(186, "Ratio of height to shadow is √3 : 1 => tan θ = √3 => θ = 60°.", "tan θ = √3 => Angle of elevation θ = 60°.")
    add(187, "Find hypotenuse using Pythagoras theorem or sin / cos ratio.", "Wire length = Hypotenuse = √(h^2 + d^2).")
    add(188, "Total height = Observer's height + height above eye level = 1.5m + 28.5 × tan 45° = 1.5 + 28.5 = 30m.", "Total height = observer height + distance × tan 45° = 1.5 + 28.5 = 30 m.")
    add(189, "tan 30° = h / 30 => h = 30 × tan 30° = 30 / √3 = 10√3.", "tan 30° = 1/√3 => h = 30/√3 = 10√3 m.")
    add(190, "Angle above the horizontal line of sight to an elevated object is the Angle of Elevation (ఊర్ధ్వ కోణము).", "Looking UP = Angle of Elevation (ఊర్ధ్వ కోణం).")
    add(191, "Angle below the horizontal line of sight to a lower object is the Angle of Depression (నిమ్న కోణము).", "Looking DOWN = Angle of Depression (నిమ్న కోణం).")
    add(192, "Find angle using sin θ = opposite / hypotenuse or cos θ = adjacent / hypotenuse.", "trig ratio value matches 60°.")
    add(193, "“Mathematics is the mirror of civilization” was stated by Lancelot Hogben.", "Memory quote: Mirror of Civilization = Hogben (హాగ్ బెన్).")
    add(194, "“Mathematics is the gateway and key to all sciences” was stated by Roger Bacon.", "Memory quote: Gateway and Key = Roger Bacon (రోజర్ బేకన్).")
    add(195, "The classic mathematical treatise “Elements” (13 books) was written by Euclid of Alexandria.", "Euclid = Father of Geometry, Author of 'Elements'.")
    add(196, "Mathematics is derived from Greek words: 'Mathema' (learning/knowledge) and 'Techne' (art/craft).", "Greek etymology: Mathema (learning) + Techne (art).")
    add(197, "“Mathematics is the science that draws necessary conclusions” was defined by Benjamin Peirce.", "Benjamin Peirce: 'Science that draws necessary conclusions'.")
    add(198, "Mathematics is inherently logical, precise, abstract, and deductive. Claiming it is 'not logical' is incorrect.", "Nature of Mathematics: Logical, Abstract, Exact, Systematic, Deductive.")
    add(199, "Affective domain (Krathwohl): Receiving, Responding, Valuing, Organization, Characterization. 'Precision' belongs to Psychomotor domain.", "Domains: Cognitive (Bloom), Affective (Krathwohl), Psychomotor (Simpson/Dave). Precision = Psychomotor.")
    add(200, "Valuing (విలువకట్టడం) is the 3rd level in Krathwohl's taxonomy of the Affective Domain.", "Affective hierarchy: Receiving -> Responding -> Valuing -> Organization -> Characterization.")

    # 201 to 240: Pedagogy, Methods, NCF, NEP, Evaluation
    add(201, "Aryabhata gave the value of π as 3.1416 (62832 / 20000) and revealed it is approximately irrational.", "Aryabhata: π ≈ 62832/20000 = 3.1416 (Aryabhatiya).")
    add(202, "Bhaskaracharya in Lilavati mentioned practical approximations including taking π = √10.", "Bhaskaracharya II: Author of Lilavati and Bijaganita, π ≈ √10.")
    add(203, "Euclid proved that the set of prime numbers is infinite (Euclid's Theorem on primes).", "Euclid: Infinitude of primes proof via contradiction.")
    add(204, "The theorem that the sum of angles of a triangle is 180° was first proven by the Pythagorean school.", "Pythagoras school: Sum of 3 angles of triangle = 2 right angles (180°).")
    add(205, "Synthesis method starts from known facts and proceeds to unknown (leads to the final product/proof).", "Analysis = Breaking down (process of discovery); Synthesis = Combining (product of thought).")
    add(206, "Comenius strongly supported deductive approaches (general principle to specific instances) in educational pedagogy.", "Deductive method: General rule -> Specific examples (Comenius).")
    add(207, "John Dewey, the progressive philosopher and father of Pragmatism, proclaimed: 'Education is life itself, not preparation for life.'", "John Dewey: 'Education is not preparation for life; education is life itself.'")
    add(208, "Inductive method proceeds from Particular examples to General rule (Concrete to Abstract).", "Inductive = Particular to General, Known to Unknown, Concrete to Abstract.")
    add(209, "Analysis method breaks the problem into parts to understand 'why' and find how the proof was discovered.", "Analysis = 'Unknown to Known' (Unveils the reasoning behind the solution).")
    add(210, "Proceeding from specific examples to general formulas is the Inductive method.", "Inductive approach: Examples -> Observation -> Generalization / Formula.")
    add(211, "Inductive method is the most natural and convenient method for students to discover and derive new mathematical formulas.", "Formula derivation in school math = Inductive method (followed by Deductive practice).")
    add(212, "Laboratory method in mathematics involves hands-on experiments, measurements, and practical verification.", "Laboratory method: 'Learning by doing' & 'Learning by observation' with mathematical equipment.")
    add(213, "Project method is an authentic purposeful activity carried out in natural settings, based on 'Learning by doing'.", "Project method (Kilpatrick / Dewey): Purposeful activity in real-life context.")
    add(214, "“A project is a bit of real life that has been imparted into the school” is the definition by Ballard.", "Memory tip: 'Bit of real life in school' = Ballard definition of project.")
    add(215, "Analysis method is lengthy and requires skilled guidance, but fosters deep logical thinking; it is not suited for quick routine syllabus completion.", "Limitation of Analysis: Time-consuming. Strength: Develops discovery & inquiry mindset.")
    add(216, "Synthetic method is concise, elegant, straightforward, and time-saving because it presents the finished proof directly.", "Synthetic method: Fast, neat, memory-friendly, time-saving.")
    add(217, "A Unit Plan outlines sub-units, learning outcomes, teaching-learning activities, and assessment; specific step-by-step teaching methods are detailed in daily Lesson Plans.", "Unit Plan = Broad overview of topics & periods; Period Lesson Plan = Specific micro-steps.")
    add(218, "Explaining mathematical concepts in one's own words represents the academic standard of Communication (వ్యక్తపరచడం).", "AP Academic Standards: Problem Solving, Reasoning & Proof, Communication, Connection, Representation.")
    add(219, "Bloom's Cognitive Domain includes Knowledge, Comprehension, Application, Analysis, Synthesis, Evaluation.", "Cognitive levels: Remember -> Understand -> Apply -> Analyze -> Evaluate -> Create.")
    add(220, "Creating student-generated meaningful problems and real-world math exploration is emphasized by NCF-2005 & APSCF-2011.", "NCF-2005 / APSCF-2011: Shift from rote learning to problem posing and problem solving.")
    add(221, "NEP-2020 emphasizes reduction in curriculum content to core essentials to make space for critical thinking and inquiry-based learning.", "NEP 2020: Focus on core elements, reduction in course content, experiential learning.")
    add(222, "“Education must move towards less content and more learning about how to think critically and solve problems” is a key vision of NEP 2020.", "NEP 2020 Key Mantra: Less content, more critical thinking and holistic development.")
    add(223, "Establishing a 'Problem Corner' / 'Ganitha Moola' via school mathematics club is recommended in APSCF-2011.", "APSCF-2011: Mathematics club activities, problem corner for fostering mathematical curiosity.")
    add(224, "NEP 2020 strongly recommends preparing bilingual teaching-learning materials (TLMs) and textbooks.", "NEP 2020 Language policy: Bilingual textbooks and learning materials for regional medium learners.")
    add(225, "Herbartian 5 steps: 1. Preparation, 2. Presentation (సమర్పణ), 3. Association / Comparison, 4. Generalization, 5. Application.", "Herbartian steps sequence: Preparation -> Presentation -> Comparison -> Generalization -> Application.")
    add(226, "“Children learn to enjoy mathematics rather than fear it” is the foundational vision of NCF-2005 and APSCF-2011.", "NCF-2005 Math Vision: Children enjoy math, see it as part of life, and talk about math.")
    add(227, "Educational guidelines for textbook and lesson design were systematically structured by educationist Frust.", "Textbook and curriculum design recommendations = Frust.")
    add(228, "In Herbartian steps, drawing common principles or mathematical rules after comparison is Generalisation (సాధారణీకరణ).", "Generalisation = Deriving the rule, formula, or law after comparing multiple examples.")
    add(229, "Anecdotal record is an objective written narrative description of significant student behavior and personality incidents.", "Anecdotal Record: Informal narrative record of student's personality traits and behavioral episodes.")
    add(230, "“Evaluation is a continuous process, forms an integral part of the total educational system” was stated by Kothari Commission (1964-66).", "Kothari Commission (1964-66): 'Evaluation is a continuous process...' (Origin of CCE).")
    add(231, "Summative assessment (సంగ్రహణాత్మక మూల్యాంకనం) is conducted at the end of an instructional term/year to evaluate overall achievement.", "Summative = End of term / course assessment for grading and certification.")
    add(232, "Formative assessment (నిర్మాణాత్మక మూల్యాంకనం) is conducted continuously during the teaching-learning process for learning feedback.", "Formative = During instruction (Assessment FOR Learning).")
    add(233, "In AP CCE Formative Assessment, the 4 tools are: 1. Student response (10m), 2. Written work / notebooks (10m), 3. Project work (10m), 4. Slip test (20m). Teacher's personal diary is not a tool.", "CCE 4 Tools: Student Reflection (10), Notebooks (10), Projects (10), Slip Test (20).")
    add(234, "Slip test carries 20 marks out of 50 total marks in Formative Assessment (highest weightage: 40%).", "Formative Assessment Weightage: Slip test has 20 marks out of 50 (highest).")
    add(235, "Association form is an open-ended / supply type item, whereas multiple choice, matching, and true/false are objective selection types.", "Objective items: True/False, Multiple Choice, Matching (selection type). Association = supply type.")
    add(236, "Odd man out questions test classification/objective reasoning, distinct from purely descriptive very short answer questions.", "Item classification: Odd-man out is an objective analytical format.")
    add(237, "Alternative response type (True/False, Yes/No, Right/Wrong) is a classic objective question format.", "Alternative response = True/False or Yes/No (objective test item).")
    add(238, "Association form is considered a very short answer supply item where learner directly supplies connected words.", "Very Short Answer = Supply type requiring concise 1-word or phrase response.")
    add(239, "Circle : 2πr :: Square : 4s is an Analogy (సాదృశ్య రూపం) type question testing relationship between perimeter formulas.", "Analogy format: A : B :: C : D (Tests pattern & structural relationship).")
    add(240, "Peg board is a learning manipulative used to visualize geometric figures, coordinate grids, and perimeters.", "Peg board / Geoboard: Visual aid for shapes, polygons, and coordinate relations.")

    print(f"Total hints prepared: {len(hints_tips)}")
    assert len(hints_tips) == 240, f"Expected 240, got {len(hints_tips)}"

    # Update questions
    for q in questions:
        qid = q["id"]
        q["hint"] = hints_tips[qid]["hint"]
        q["memory_tip"] = hints_tips[qid]["memory_tip"]

    with open("maths_questions.json", "w", encoding="utf-8") as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)

    print("Successfully updated maths_questions.json with 240 hints and memory tips!")

if __name__ == "__main__":
    generate_maths_hints()
