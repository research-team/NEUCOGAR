package org.necougor.parser.model.image;


public class Root
{
    private MxCell[] mxCell;

    public MxCell[] getMxCell ()
    {
        return mxCell;
    }

    public void setMxCell (MxCell[] mxCell)
    {
        this.mxCell = mxCell;
    }

    @Override
    public String toString()
    {
        return "ClassPojo [mxCell = "+mxCell+"]";
    }
}