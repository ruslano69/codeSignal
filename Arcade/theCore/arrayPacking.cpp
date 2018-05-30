int arrayPacking(std::vector<int> a) {
 
    int M=0;
    int shift = 0;
    for(int i = 0;i < a.size(); i++)
    {
        M += (a[i] << shift);
        shift += 8;
    }
    return M;

}
